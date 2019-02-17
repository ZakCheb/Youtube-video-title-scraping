from bs4 import BeautifulSoup
HEADERS={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Host':"www.youtube.com",
        'Accept':"*/*",
        'Conection':'Closed',
        }

import requests as req

resp = req.get("https://www.youtube.com/feed/trending",headers=HEADERS)
#print(resp.text)

data= BeautifulSoup(resp.text,'html.parser')
titles=data.find_all(class_="yt-uix-tile-link")
for i in titles:
    print(i.text)
#print(dir(titles[0]))
