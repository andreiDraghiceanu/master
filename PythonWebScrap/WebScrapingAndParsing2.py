from importlib import reload
import os
import urllib.request
import site

os.system('py -2 -m pip install --upgrade pip')
reload(site)

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    print("BeautifulSoup lib not found!")
    import pip
    cmd = 'py -2 -m pip install BeautifulSoup4'
    print("Please enter the root password to install the required package!")
    os.system(cmd)
    reload(site)

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs(source, 'lxml')

nav = soup.nav

#print(nav)

# for url in nav.find_all('a'):
#     print(url.get('href'))

# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

for div in soup.find_all('div', class_='body'):
    print(div.text)