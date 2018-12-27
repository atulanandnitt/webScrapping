# main file


import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from to_findAllUrls import findAllUrls



def webScrap(tempUrl):
    r = requests.get(tempUrl)
    soup = BeautifulSoup(r.content)
    text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    return c
    


if __name__ == "__main__":
    WordCounter = Counter()    
    url = "https://hiverhq.com/" 
    allUrls={"https://hiverhq.com/"}
    QueueAllUrl=["https://hiverhq.com/"]
    
    while len(QueueAllUrl)>0:
        tempUrl = QueueAllUrl.pop(0)
        allUrls = findAllUrls(tempUrl,allUrls,QueueAllUrl)
        
    #print("webpages in this website ", allUrls)
    for tempUrl in allUrls:
        #print("scrapping : ",tempUrl)
        WordCounter += webScrap(tempUrl)
        
       
    sorted_by_value = sorted(WordCounter.items(), key=lambda kv: kv[1])
    
    for item in sorted_by_value[-5:][::-1]:
        print(item[0])
