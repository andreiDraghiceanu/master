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

#table = soup.table
table = soup.find('table')
#print(table)

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row) 


