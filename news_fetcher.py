import requests
from datetime import datetime, timedelta
import os

def fetch_finance_news(api_key):
    # Define the time range for the last 12 hours
    now = datetime.utcnow()
    time_from = (now - timedelta(hours=12)).strftime('%Y%m%dT%H%M')

    # Alpha Vantage Market News & Sentiment API endpoint
    url = "https://www.alphavantage.co/query"
    
    # Compose the request parameters
    params = {
        "function": "NEWS_SENTIMENT",
        "topics": "business OR technology OR financial_markets",
        "time_from": time_from,
        "sort": "RELEVANCE",  # LATEST, EARLIEST, RELEVANCE
        "limit": "10",
        "apikey": api_key
    }

    # Make the request
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("feed", [])  # Correct key based on provided output
        formatted_articles = []
        for article in articles:
            formatted_article = {
                'title': article['title'],
                'description': article.get('summary', 'No summary available'),
                'url': article['url'],
                'image': article.get('banner_image', ''),  # Assuming you want to include the banner image if available
                'source': article['source']
            }
            formatted_articles.append(formatted_article)
            print(f"Title: {article['title']}")
            print(f"Description: {article.get('summary', 'No summary available')}\n")
        return formatted_articles
    else:
        print(f"HTTP error occurred: {response.status_code} {response.reason}")

    return []

# Example usage
if __name__ == '__main__':
    api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')  # Ensure this environment variable is correctly set
    market_news = fetch_finance_news(api_key)
