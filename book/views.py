import json
import os
import threading

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
# Create your views here.
from book import utils
from book.models import Novel, Chapter
from book.utils import save_book, get_chapter_content, __search_book
from main import get_json_data
from django.views.decorators.csrf import csrf_exempt

from shuchong1.settings import BOOK_SRC_URL
from django.core.paginator import Paginator


def index(request):
  books = Novel.objects.all()
  return render(request, 'novel_list.html', {'books': books})


def download(request):
  book_id = request.GET['id']

  if book_id not in settings.BOOK_DOWNLOAD_QUEUE:
    settings.BOOK_DOWNLOAD_QUEUE.add(book_id)
    # print(u'新线程开始....')
    threading.Thread(target=save_book, args=[settings.BOOK_SRC_URL + '/' + book_id, ]).start()

  return HttpResponse('downloading...')


@csrf_exempt
def chapter(request):
  body = json.loads(request.body)
  bookId = int(body['id'])
  chapterNo = int(body['chapterno'])
  spiderUrl = Chapter.objects.get(novel_id=bookId, no=chapterNo).context_url
  name = Chapter.objects.get(novel_id=bookId, no=chapterNo).name
  context = get_chapter_content(BOOK_SRC_URL + spiderUrl).split('\xa0\xa0\xa0\xa0')

  data = {
    'context': context,
    'name': name
  }
  return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def catalog(request):
  bookId = request.GET['id']
  calalog = Chapter.objects.filter(novel_id=bookId).values()
  info = Novel.objects.filter(id=bookId).values()[0]
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
  book_list = Novel.objects.all().values()
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
