# -*- coding: CP949 -*-
import requests
from bs4 import BeautifulSoup


def _spider():
    url = 'http://m.news.naver.com/rankingList.nhn?type=section'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    link = soup.select('#politics1 > a')[0]  # beautifulSoup is use array
    href = 'http://m.news.naver.com' + link.get('href')
    article_crawler(href)  # send to text crawler

def article_crawler(article_link):
    source_code = requests.get(article_link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    article_text = soup.select('div.newsct_article > div#dic_area')
    for content in article_text:
        print(content.get_text())
        article_content = content.find_all(text=True)
        #print(article_content) print text + source code

_spider()
