import json
import os
import threading

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
# Create your views here.
from book import utils
from book.models import Novel, Chapter
from book.utils import save_book
from main import get_json_data


def index(request):
  books = Novel.objects.all()
  return render(request, 'novel_list.html', {'books': books})


def demo(request):
  area = request.GET['area']
  type = request.GET['type']
  year = request.GET['year']

  filepath = 'films&area=%s&type=%s&year=%s.json' % (area, type, year)
  # 如果文件不存在
  if os.path.exists(filepath) is not True:
    get_json_data(area, type, year)

  # if time.localtime(os.path.getmtime(filepath)).tm_mday != time.localtime(time.time()).tm_mday:
  #   get_json_data(area, type, year)
  f = open(filepath, encoding='utf-8')
  return HttpResponse(f.read(), content_type='application/json')


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


def download(request):
  book_id = request.GET['id']

  if book_id not in settings.BOOK_DOWNLOAD_QUEUE:
    settings.BOOK_DOWNLOAD_QUEUE.add(book_id)
    # print(u'新线程开始....')
    threading.Thread(target=save_book, args=[settings.BOOK_SRC_URL + '/' + book_id, ]).start()

  return HttpResponse('downloading...')


def catalog(request, book_id):
  bookInfo = Novel.objects.get(id=book_id)
  chapters = Chapter.objects.filter(novel_id_id=book_id)

  len = chapters.__len__()

  # tmp1 = []
  # for chapter in chapters:
  #   tmp1.append({'chapter_name': chapter.name, 'src': chapter.context_url})
  #
  # data = {}
  # data['chapters'] = tmp1
  # data['info'] = bookInfo.description
  # data['cover'] = bookInfo.imgSrc
  # data['author'] = bookInfo.author
  # data['name'] = bookInfo.name
  # return HttpResponse(json.dumps(data), content_type="application/json")
  return render(request, 'chapterlist.html', {'chapters': chapters, 'bookInfo': bookInfo, 'len': len})


def catalogtojson(request, book_id):
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
  return HttpResponse(json.dumps(data), content_type="application/json")
  # return render(request, 'chapterlist.html', {'chapters': chapters, 'bookInfo': bookInfo, 'len': len})


def get_all_books(request):
  books = Novel.objects.all()
  data = []
  for book in books:
    data.append(
      {'id': book.id, 'name': book.name, 'cover': book.imgSrc, 'descrip': book.description, 'author': book.author})

  return HttpResponse(json.dumps(data), content_type="application/json")
