import requests
import os

def fetch_finance_news(api_key,industry):
    url = 'https://newsapi.org/v2/everything'
    parameters = {
        'q': industry,  # Query for industry news
        'sortBy': 'publishedAt',  # Sort by most recent
        'apiKey': api_key,  # Your API key
    }
    response = requests.get(url, params=parameters)
    news_data = response.json()
    return news_data['articles'][:5]  # Return the first 5 articles


news_api_key=os.environ.get('NEWS_API_KEY')
finance_news = fetch_finance_news(news_api_key, 'finance')
