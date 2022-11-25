import requests
import sys
from bs4 import BeautifulSoup

url = str(sys.argv[1])

r = requests.get(url)

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
    content += "\n" + part.get_text()

result = "Article title: " + headline
result += "\nBy: " + author
result += "\nLast updated on: " + timestamp
result += "\n" + content

output = open('scraped_news.txt', 'w')
output.write(result)
output.close()

print("Done.")
print("Open scraped_news.txt to see results!")