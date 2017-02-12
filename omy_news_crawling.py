# -*- coding: CP949 -*-
import requests
from bs4 import BeautifulSoup


def _spider():
    url = 'http://m.ohmynews.com/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    link = soup.select('li.row_thumb > a.link_thumb')[0]  # beautifulSoup is use array
    """
    select daily first news in politcs
    """
    href = 'http://m.ohmynews.com' + link.get('href')
    article_crawler(href)  # send to text crawler


def article_crawler(article_link):
    source_code = requests.get(article_link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    article_text = soup.select('div.at_contents')
    for content in article_text:
        print(content.get_text())
        article_content = content.find_all(text=True)
        #print(article_content)

_spider()
