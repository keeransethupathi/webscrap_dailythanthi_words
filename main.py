# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:29:52 2022

@author: keerans
"""


import requests
from bs4 import BeautifulSoup
import re
import tamil



# filter url 
def multi_extract_url(urls):
    def filter_url(s):
        return re.findall(r'(https?://www.dailythanthi.com/\S+)', s)
    extract_urls=[]
    for s in urls:
        extract_urls.append(filter_url(str(s)))
    return extract_urls

# merge sublist 
def merge_url(extract_urls):
    mergeurl = []
    for i in extract_urls:
        mergeurl += i
    return mergeurl 

# extract url

def get_url(url):
    urls=[]
    for i in url:
        reqs = requests.get(i)
        soup = BeautifulSoup(reqs.text, 'html.parser')           
        urls2 = []   
        for link in soup.find_all('a'):
            urls2.append(link.get('href'))
        urls.extend(urls2)
    return urls

# 

def Tamilwebscraping(url):
    def webscraping(url):
        # read url
        html = requests.get(url).content
        soup = BeautifulSoup(html, features="html.parser")  
        # get words
        text = soup.get_text()
        # filter tamil words
        taletters = tamil.utf8.get_letters(text)
        frequency = {}
        for x,word in enumerate(tamil.utf8.get_tamil_words(taletters)):
            frequency[word] = 1 + frequency.get(word,0)
        return list(frequency)
    
    v = url[1:100]
    y = []
    for x in v:
        y.extend(webscraping(x))
        y = list(dict.fromkeys(y))
    total = []
    for i in [y]:
        total += i
    return i