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


def get_update_time(soup):
  return soup.select('#info > p')[2].text.split('：')[1]


def get_latest_chapter(soup):
  return soup.select('#info > p')[3].select('a')[0].text


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
  desc = get_description(soup)
  imgSrc = get_img_src(soup)
  chapter_list = get_chapter_list(soup)
  author = get_author_name(soup)
  updateTime = get_update_time(soup)
  latestChapter = get_latest_chapter(soup)
  if Novel.objects.filter(name=book_name).count() == 0:
    Novel.objects.create(name=book_name, description=desc,
                         imgSrc=imgSrc, author=author,
                         updateTime=updateTime, latestChapter=latestChapter)

  book_id = Novel.objects.get(name=book_name).id
  for chapter in chapter_list:
    chapter_name = chapter.text
    if Chapter.objects.filter(novel_id_id=book_id, name=chapter_name).count() == 0:
      Chapter.objects.create(novel_id_id=book_id, no=chapter_list.index(chapter) + 1,
                             name=chapter_name, context_url=chapter['href'])
      print(chapter_name)


def __search_book(keyword):
  soup = bs(get_html_doc('https://www.xbiquge6.com/search.php?keyword=%s' % keyword), 'lxml')
  res = soup.select('.result-item ')
  rep_li = []
  for item in res:
    desc = item.select('p.result-game-item-desc')[0].text
    imgSrc = item.select('a.result-game-item-pic-link > img')[0]['src']
    tmp = item.select('a.result-game-item-title-link')[0]
    name = tmp['title']
    url = tmp['href']
    author = item.select('p.result-game-item-info-tag')[0].select('span')[1].text
    latestChapter = item.select('a.result-game-item-info-tag-item')[0].text
    updateTime = item.select('p.result-game-item-info-tag')[2].select('span')[1].text
    rep_li.append({
      'name': name,
      'imgSrc': imgSrc,
      'url': url,
      'description': desc,
      'author': author.strip(),
      'updateTime': updateTime,
      'latestChapter': latestChapter.strip(),
    })
  return rep_li


if __name__ == '__main__':
  # soup = bs(get_html_doc('https://www.xbiquge6.com/74_74821/'), 'lxml')
  # print(get_update_time(soup), get_latest_chapter(soup))
  # print(search_book('完美世界'))
  pass
