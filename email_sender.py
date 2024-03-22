import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from news_fetcher import fetch_finance_news


def send_news_email(from_email, to_email, subject, news_articles, sendgrid_api_key):
    content = "<h1>Finance News Digest</h1>"
    for article in news_articles:
        content += f"<p><a href='{article['url']}'>{article['title']}</a></p>"
    
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )
    
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

# Example usage
sg_api_key=os.environ.get('SENDGRID_API_KEY')
# from_email = 'lomvax@gmail.com'  # Replace with your email
# to_email = 'lomvax@gmail.com'  # Replace with recipient's email
# subject = 'Your Daily Digest'
# finance_news = fetch_finance_news('fbf80615340a45e7a220852034904417')
# send_news_email(from_email, to_email, subject, finance_news, sg_api_key)