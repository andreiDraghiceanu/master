import os
import site
import urllib.request
from importlib import reload

os.system('py -2 -m pip install --upgrade pip')
os.system('py -2 -m pip install --upgrade lxml')
os.system('py -2 -m pip install --upgrade html5lib')
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

#print(soup)
#print(soup.title)
#print(soup.p)
#print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

#print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))







