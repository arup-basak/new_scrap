from bs4 import BeautifulSoup
import requests

def get_time_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Look for the time in the specific div class where Indian Express seems to place it
    time_element = soup.find('div', {'class': 'm-story-meta__credit'})

    if time_element is not None:
        return time_element.text.strip()

    return "Time not found"

url = "https://indianexpress.com/article/cities/kolkata/bjp-workers-clash-with-police-during-barrackpore-protest-face-lathi-charge-9133637/"
print(get_time_from_url(url))
