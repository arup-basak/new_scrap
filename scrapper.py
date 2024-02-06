from bs4 import BeautifulSoup
import requests

def scrap(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.title.text)
    except:
        pass

    
