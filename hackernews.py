import requests
from bs4 import BeautifulSoup
response=requests.get(" https://news.ycombinator.com/")
contents=response.text
soup=BeautifulSoup(contents,"html.parser")
headings=[]
links=[]
scores=[]

for heading in soup.find_all('span',class_="titleline"):
    link=heading.find("a")
    headings.append(link.get_text())
    links.append(link.get("href"))
for score in soup.find_all("span",class_="score"):
    scores.append(score.get_text())

print(headings)
print(links)
print(scores)
