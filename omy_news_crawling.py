# -*- coding: CP949 -*-
import requests
import codecs
from bs4 import BeautifulSoup

def _spider():
    url = 'http://www.ohmynews.com/NWS_Web/ArticlePage/Total_Article.aspx?PAGE_CD=C0400'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    link = soup.select('dt > a')[0]
    href = 'http://www.ohmynews.com/' + link.get('href')
    # print(href)
    article_crawler(href)

def article_crawler(article_link):
    source_code = requests.get(article_link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    article_text = soup.select('div.article_view > div.at_contents')
    for content in article_text:
        article_content = content.find_all(text=True)
        print(article_content)

_spider()
