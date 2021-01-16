from bs4 import BeautifulSoup
import requests

'''
with open('simple.html') as html_file:
  soup = BeautifulSoup(html_file, 'lxml')

#Cleans up HTML with indendation
#print(soup.prettify())

match = soup.title.text #Getting only the text tag
#print(match)

#article = soup.find('div', class_='article')
#finds only first article

for article in soup.find_all('div', class_='article'): #returns a list

  headline = article.h2.a.text
  print(headline)

  summary = article.p.text #have to unrap-ish
  print(summary)

  print()

'''

## THis chunk takes text from websites  https://www.foxnews.com/
#source = requests.get('http://coreyms.com').text
source = requests.get('https://www.foxnews.com').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())