import requests
import sys
from bs4 import BeautifulSoup

url = str(sys.argv[1])

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
headline = soup.find("span", attrs={"data-qa":"headline-text"})

print(headline.string)

with open('news.txt', 'w') as output:
    output.write(soup.prettify())