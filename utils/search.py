import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

headers = {'x-api-key': os.getenv("SCRAP_IT_API")}


def search_news(keyword):
    api_url = 'https://api.scrape-it.cloud/scrape/google'
    params = {
        'q': keyword,
        'domain': 'google.com',
        'tbm': 'nws'
    }
    response = requests.get(api_url, params=params, headers=headers)
    data = response.json()
    news = data['newsResults']
    df = pd.DataFrame(news)
    return df['link'].to_numpy()
