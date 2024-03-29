import requests
from datetime import datetime, timedelta
import os

def fetch_finance_news(api_key, category="business",language="en", country="us"):
    # Calculate the date range for the last 12 hours
    to_date = datetime.utcnow()
    from_date = to_date - timedelta(hours=12)
    to_date_str = to_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    from_date_str = from_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    # keywords="finance OR economy OR tbilisi OR tech OR stock market"

    url = "https://gnews.io/api/v4/top-headlines"
    # url = "https://gnews.io/api/v4/search"
    params = {
        "category": category,
        # "q": keywords,
        # "in": "content",
        "lang": language,
        "country": country,
        # "from": from_date_str,
        # "to": to_date_str,
        "max": "10",
        "sortby": "relevance",
        "token": api_key,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}\n")
        return articles
    else:
        print(f"HTTP error occurred: {response.status_code} {response.reason}")

    return []

# Example usage
if __name__ == '__main__':
    gnews_api_key = os.environ.get('GNEWS_API_KEY')  # Ensure this environment variable is correctly set
    finance_news = fetch_finance_news(gnews_api_key)
