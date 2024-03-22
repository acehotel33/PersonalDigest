import requests
import os

def fetch_finance_news(api_key, country="us",category="business"):
    url = 'https://newsapi.org//v2/top-headlines'
    parameters = {
        'sortBy': 'relevancy',  # Sort by relevance to the keywords
        'pageSize': 10,  # Limit to 10 articles
        'apiKey': api_key,
        'category':category,
        'country':country,
    }

    try:
        response = requests.get(url, params=parameters)
        # Check if the response was successful
        response.raise_for_status()
        news_data = response.json()
        print(news_data)  # Add this line to debug the API response
        return news_data['articles'][:10]  # Return the first 5 articles
    except requests.exceptions.HTTPError as http_err:
        # Specific HTTP errors (e.g., invalid API key, exceeding rate limits)
        print(f'HTTP error occurred: {http_err}')  # Python 3.6+
    except requests.exceptions.ConnectionError as conn_err:
        # Network problems, such as DNS failures, refused connections, etc
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        # Request timed out
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        # Catch-all for other request-related errors
        print(f'Error occurred: {req_err}')
    return []  # Return an empty list in case of error


news_api_key=os.environ.get('NEWS_API_KEY')

finance_news = fetch_finance_news(news_api_key)