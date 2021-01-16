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

import re  #needed to convert string of words into list of words
'''
mystr = 'This is a string, with words!'
wordList = re.sub("[^\w]", " ",  mystr).split()
print(wordList)
'''
#soup stuff 
## THis chunk takes text from websites  
#source = requests.get('http://coreyms.com').text
#source = requests.get('https://www.foxnews.com').text

#This segment takes user pasted URL
link = input("Please enter the URL: ")
source = requests.get(link).text


soup = BeautifulSoup(source, 'lxml')
string_soup = soup.get_text()  #turns soup object into string
list_soup = re.sub("[^\w]", " ",  string_soup).split()
print(list_soup)


#print(list_soup)  don't work
