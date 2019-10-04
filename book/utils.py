import re

import requests
from bs4 import BeautifulSoup as bs
from datetime import  datetime
from book.models import Novel, Chapter
import django.utils.timezone as timezone

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
  res = soup.select('dd > a')
  res_list = []
  for item in res:
    res_list.append({
      'name': item.text,
      'context_url': item['href']
    })
  return res_list


def get_chapter_content(content_url):
  html = get_html_doc(content_url)
  soup = bs(html, 'lxml')
  context = soup.select('#content')[0].text.split('\xa0\xa0\xa0\xa0')
  name = soup.select('.bookname > h1')[0].text
  return {
    'context': context,
    'name': name
  }


def download(book_url):
  soup = bs(get_html_doc(book_url), 'lxml')
  biqugePath = book_url.split('/')[3]
  book_name = get_book_name(soup)
  desc = get_description(soup)
  imgSrc = get_img_src(soup)
  chapter_list = get_chapter_list(soup)
  author = get_author_name(soup)
  updateTime = get_update_time(soup)
  latestChapter = get_latest_chapter(soup)
  return {
    'name': book_name,
    'description': desc,
    'imgSrc': imgSrc,
    'author': author,
    'updateTime': updateTime,
    'latestChapter': latestChapter,
    'biqugePath': biqugePath,
    'chapters': chapter_list
  }


def update_book(book_url):
  bookInfo = download(book_url)
  chapters = bookInfo['chapters']
  lastChapterOnSearch = chapters[-1]
  Novel_now = Novel.objects.filter(name=bookInfo['name'])  # 当前操作的小说对象
  Novel_now.update(updateTimeOnServer=timezone.now())
  novel_id = Novel_now.values_list()[0]
  lastChapterOnDb = list(Chapter.objects.filter(novel_id=novel_id).values())[-1]
  if lastChapterOnSearch['name'] != lastChapterOnDb['name']:
    Novel_now.update(latestChapter=bookInfo['latestChapter'],
                     updateTime=bookInfo['updateTime'])
    no = lastChapterOnDb['no']
    index = chapters.index({'name': lastChapterOnDb['name'],
                            'context_url': lastChapterOnDb['context_url']})
    len = chapters.__len__()
    queryList = []
    for i in range(index + 1, len):
      queryList.append(Chapter(novel_id_id=novel_id, no=i,
                               name=chapters[i]['name'], context_url=chapters[i]['context_url']))


def save_book(book_url):
  bookInfo = download(book_url)
  chapter_list = bookInfo['chapters']
  if Novel.objects.filter(name=bookInfo['name']).count() == 0:
    Novel.objects.create(name=bookInfo['name'], description=bookInfo['description'],
                         imgSrc=bookInfo['imgSrc'], author=bookInfo['author'],
                         biqugePath=bookInfo['biqugePath'],
                         updateTime=bookInfo['updateTime'], latestChapter=bookInfo['latestChapter'])
    book_id = Novel.objects.get(name=bookInfo['name']).id
    querySetList = []
    for chapter in chapter_list:
      querySetList.append(Chapter(novel_id_id=book_id, no=chapter_list.index(chapter) + 1,
                                  name=chapter['name'], context_url=chapter['context_url']))
    Chapter.objects.bulk_create(querySetList)


def __search_book(keyword):
  soup = bs(get_html_doc('https://www.xbiquge6.com/search.php?keyword=%s' % keyword), 'lxml')
  res = soup.select('.result-item ')
  rep_li = []
  for item in res:
    desc = item.select('p.result-game-item-desc')[0].text
    imgSrc = item.select('a.result-game-item-pic-link > img')[0]['src']
    tmp = item.select('a.result-game-item-title-link')[0]
    name = tmp['title']
    biqugePath = tmp['href']
    author = item.select('p.result-game-item-info-tag')[0].select('span')[1].text
    latestChapter = item.select('a.result-game-item-info-tag-item')[0].text
    updateTime = item.select('p.result-game-item-info-tag')[2].select('span')[1].text
    rep_li.append({
      'name': name,
      'imgSrc': imgSrc,
      'biqugePath': biqugePath.split('/')[3],
      'description': desc,
      'author': author.strip(),
      'updateTime': updateTime,
      'latestChapter': latestChapter.strip(),
    })
  return rep_li


if __name__ == '__main__':
  print(datetime.now())
  # d1 = datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
  # d2 = datetime.strptime('2012-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
  # delta = d1 - d2
  # print(delta.days)
  # print(datetime.now().strptime())
  # print(str(datetime.strptime(datetime.now(), )))

  # soup = bs(get_html_doc('https://www.xbiquge6.com/74_74821/'), 'lxml')
  # print(get_update_time(soup), get_latest_chapter(soup))
  # print(search_book('完美世界'))
  # print([1, 2, 3][-1])
  # print([{'name': 'oyy'}, {'name': 'oyy2'}].index({'name': 'oyy2'}))
  # pass

