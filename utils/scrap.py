from bs4 import BeautifulSoup
import requests
from sentiment import get_sentiment

url = "https://www.deccanherald.com/india/utter-state-of-lawlessness-in-bengal-bjp-s-fact-finding-team-1239104.html"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    main_content = soup.find('body')

    if main_content:
        main_text = main_content.get_text()
        print(get_sentiment(main_text))
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")