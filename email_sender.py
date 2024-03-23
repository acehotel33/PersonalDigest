import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from news_fetcher import fetch_finance_news
from jinja2 import Environment, FileSystemLoader, select_autoescape

def send_news_email(from_email, to_email, subject, news_articles, sendgrid_api_key):
    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(searchpath="./templates"),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    template = env.get_template('email_template.html')
    content = template.render(articles=news_articles)  # Render the template with the articles
    
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

# Example usage setup
if __name__ == '__main__':
    sg_api_key = os.environ.get('SENDGRID_API_KEY')
    news_api_key = os.environ.get('GNEWS_API_KEY')
    from_email = os.environ.get('FROM_EMAIL')  # Use environment variable for sender email
    to_email = os.environ.get('TO_EMAIL')  # Use environment variable for recipient email
    subject = 'Your Daily Finance Digest'
    finance_news = fetch_finance_news(news_api_key)
    send_news_email(from_email, to_email, subject, finance_news, sg_api_key)
