from importlib import reload
import os
import urllib.request
import site
import bs4 as bs

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)

