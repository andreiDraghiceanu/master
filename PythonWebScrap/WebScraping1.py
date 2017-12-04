from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

match = soup.title.text
print(match)

article = soup.find('div', class_='article')
print(article)

print('\n' * 3)

headline = article.h2.a.text
print(headline)

print('\n' * 3)

summary = article.p.text
print(summary)

print('\n' * 3)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)


print('\n' * 3)



