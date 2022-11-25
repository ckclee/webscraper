import requests
import sys
from bs4 import BeautifulSoup
import os

url = input("Please enter a valid Washington Post URL:\n")
print("\n ... \n")

try:
    r = requests.get(url)
except:
    print('Invalid URL, please try again')
    
if(r.status_code != 200):
    if(r.status_code == 404):
        print("Error getting news, status code is: " +
              str(r.status_code))
        raise Exception(
            'It looks like this page dont exists! Check if your URL is valid')
    else:
        print("Error getting news, status code is: " +
              str(r.status_code))
        raise Exception(
            'Check if the URL is valid, if you have an internet connection or try later!')

soup = BeautifulSoup(r.content, 'html.parser')

headline_tag = soup.find(attrs={"data-qa":"headline-text"})
author_tag = soup.find(attrs={"data-qa":"author-name"})
timestamp_tag = soup.find(attrs={"data-qa":"timestamp"})
content_tag = soup.find_all(attrs={"data-el":"text"})

headline = headline_tag.get_text()
author = author_tag.get_text()
timestamp = timestamp_tag.get_text()
content = ""
for part in content_tag:
    content += "\n\n" + part.get_text()

result = "Article title: " + headline
result += "\nBy: " + author
result += "\nLast updated on: " + timestamp
result += "\n" + content

output = open('scraped_news.txt', 'w')
output.write(result)
output.close()

print("Done.")
print("Open scraped_news.txt to see results!")

os.startfile('scraped_news.txt')