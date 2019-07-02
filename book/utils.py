import re

import requests
from bs4 import BeautifulSoup as bs
from book.models import Novel, Chapter

header = {
  'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'
}

url = 'https://www.xbiquge6.com'


def get_html_doc(url):
  response = requests.get(url, header)
  response.encoding = 'utf-8'
  return response.text


def get_book_name(soup):
  return soup.select('h1')[0].text


def get_img_src(soup):
  return soup.select('#fmimg > img')[0]['src']


def get_author_name(soup):
  return soup.select('#info > p')[0].text.split('：')[1]


def get_description(soup):
  return soup.select('#intro > p')[0].text


def get_chapter_list(soup):
  return soup.select('dd > a')


def get_chapter_content(content_url):
  html = get_html_doc(content_url)
  soup = bs(html, 'lxml')
  return soup.select('#content')[0].text


def save_book(book_url):
  soup = bs(get_html_doc(book_url), 'lxml')
  book_name = get_book_name(soup)
  book_description = get_description(soup)
  book_cover_img_src = get_img_src(soup)
  chapter_list = get_chapter_list(soup)
  author = get_author_name(soup)
  try:
    Novel.objects.get(name=book_name)
  except:
    Novel.objects.create(name=book_name,
                         description=book_description,
                         imgSrc=book_cover_img_src,
                         author=author)
  book_id = Novel.objects.get(name=book_name).id
  for chapter in chapter_list:
    chapter_name = chapter.text
    try:
      Chapter.objects.get(novel_id_id=book_id, name=chapter_name)
    except:
      Chapter.objects.create(novel_id_id=book_id, no=chapter_list.index(chapter) + 1, name=chapter_name,
                             context_url=chapter['href'])
      # print(chapter_name)


if __name__ == '__main__':
  pass