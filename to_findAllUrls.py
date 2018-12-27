import urllib.request
import re
from bs4 import BeautifulSoup


def findAllUrls(parentURL,allUrls,QueueAllUrl):
    html_page = urllib.request.urlopen(parentURL)
    soup = BeautifulSoup(html_page)

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        link1 = link.get('href')
        
        if "hiverhq" in link1:
            allUrls.add(link1)
            if link1 not in allUrls:
                QueueAllUrl.append(link1)

    for link in soup.findAll('a', attrs={'href': re.compile("^/")}):
        link1 = link.get('href')
        baseUrl = parentURL
        fullUrl = baseUrl+link1[1:]

        allUrls.add(fullUrl)
        if "hiverhq" in link1:
            if link1 not in allUrls:
                QueueAllUrl.append(link1)
                
                
    return allUrls
