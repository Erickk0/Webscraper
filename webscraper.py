from bs4 import BeautifulSoup
import requests


url = input('Enter URL: ')
tagsearch = input('Enter a tag: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrapewebsite(url):
    pagetoScrape = requests.get(url, headers=headers)
    soup = BeautifulSoup(pagetoScrape.content,'lxml')

    if tagsearch is not None:
        tags = soup.find_all(tagsearch)
    else:
        tags = soup.find_all('title')

    print(soup.text)

    for tag in tags:
        print(tag)


scrapewebsite(url)