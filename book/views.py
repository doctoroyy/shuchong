import json
import os
import threading
from time import sleep

import django.utils.timezone as timezone

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
# Create your views here.
from book import utils
from book.models import Novel, Chapter
from book.utils import save_book, get_chapter_content, __search_book, update_book
from main import get_json_data
from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator


def index(request):
  books = Novel.objects.all()
  return render(request, 'novel_list.html', {'books': books})


def download(request):
  biqugePath = request.GET['id']
  if Novel.objects.filter(biqugePath=biqugePath).count() == 0:
    # print('进入线程')
    threading.Thread(target=save_book, args=[settings.BOOK_SRC_URL + '/' + biqugePath, ]).start()
  return HttpResponse('downloading...')


def update(request):
  book_id = request.GET['id']
  update_book(settings.BOOK_SRC_URL + '/' + book_id)
  return HttpResponse('更新！')


@csrf_exempt
def chapter(request):
  body = json.loads(request.body)
  biqugePath = str(body['id'])
  novel_id = dict(Novel.objects.filter(biqugePath=biqugePath).values()[0])['id']
  chapterNo = int(body['chapterno'])
  context_url = Chapter.objects.filter(novel_id=novel_id, no=chapterNo).values()[0]['context_url']
  data = get_chapter_content(settings.BOOK_SRC_URL + context_url)

  return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def catalog(request):
  biqugePath = request.GET['id']
  novel_now = Novel.objects.filter(biqugePath=biqugePath).values()[0]
  d1 = timezone.now()
  d2 = novel_now['updateTimeOnServer']
  if (d1 - d2).days >= 1:
    threading.Thread(target=update_book, args=[settings.BOOK_SRC_URL + '/' + biqugePath, ]).start()
    sleep(1)
  info = {
    'name': novel_now['name'],
    'description': novel_now['description'],
    'author': novel_now['author'],
    'imgSrc': novel_now['imgSrc'],
    'latestChapter': novel_now['latestChapter'],
    'updateTime': novel_now['updateTime'],
    'biqugePath': novel_now['biqugePath'],
    'tags': novel_now['tags'],
  }
  bookId = novel_now['id']
  calalog = Chapter.objects.filter(novel_id=bookId).values()
  data = {
    'code': 0,
    'data': {
      'chapters': list(calalog),
      'bookInfo': dict(info),
    }
  }
  return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def get_all_books(request):
  body = json.loads(request.body)
  page = body['page']
  page_size = body['pageSize']
  book_list = Novel.objects.all().values(
    'name',
    'description',
    'author',
    'imgSrc',
    'latestChapter',
    'updateTime',
    'biqugePath',
    'tags',
  )
  p = Paginator(book_list, page_size)
  total = book_list.__len__()
  pages = total / page_size
  if total % page_size != 0:
    pages += 1
  data = {
    'page': page,
    'pageSize': page_size,
    'total': total,
    'data': p.page(page).object_list
  }

  return HttpResponse(json.dumps(data))


@csrf_exempt
def search_book(request):
  body = json.loads(request.body)
  keyword = body['keyword']
  books = __search_book(keyword)
  return HttpResponse(json.dumps(books))


# 历史
def catalog2(request, book_id):
  bookInfo = Novel.objects.get(id=book_id)
  chapters = Chapter.objects.filter(novel_id_id=book_id)

  len = chapters.__len__()

  tmp1 = []
  for chapter in chapters:
    tmp1.append({'chapter_name': chapter.name, 'src': chapter.context_url})

  data = {}
  data['chapters'] = tmp1
  data['info'] = bookInfo.description
  data['cover'] = bookInfo.imgSrc
  data['author'] = bookInfo.author
  data['name'] = bookInfo.name
  # return HttpResponse(json.dumps(data), content_type="application/json")
  return render(request, 'chapterlist.html', {'chapters': chapters, 'bookInfo': bookInfo, 'len': len})


def chapter_detail(request, book_id, chapter_no):
  bookInfo = Novel.objects.get(id=book_id)
  try:
    chapter = Chapter.objects.get(novel_id_id=book_id, no=chapter_no)
    context_url = settings.BOOK_SRC_URL + chapter.context_url
    context = utils.get_chapter_content(context_url).split('\xa0\xa0\xa0\xa0')
    chapter_name = chapter.name
    ctx = {
      'chapter_no': chapter_no,
      'chapter_name': chapter_name,
      'context': context,
      'bookInfo': bookInfo,
    }
  except:
    ctx = {
      'chapter_no': chapter_no,
      'chapter_name': '已经是最后一章了...',
      'context': '',
      'bookInfo': bookInfo
    }

  return render(request, 'chapter_detail.html', ctx)

# 历史
