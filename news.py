import requests 
from bs4 import BeautifulSoup
url="https://www.bbc.com/news"

response=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})

soup=BeautifulSoup(response.content,'html.parser')
headlines=soup.find_all('h3')
with open("headlines.txt","w",encoding="utf-8") as file:
    for h in headlines:
        text=h.get_text(strip=True)
        if text:
            file.write(text+"\n")
print("Scraping completed")
