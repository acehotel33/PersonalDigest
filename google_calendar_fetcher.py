import datetime
from dateutil import tz
import os
from zoneinfo import ZoneInfo
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
import boto3

# SCOPES specifies the access your application has to the user's data
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_secret():
    secret_name = "gcloud_service_key"
    region_name = "eu-north-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)




def fetch_calendar_events():
    # --- For accessing gcloud_service_key via AWS Secrets ---
    secret = get_secret()
    creds = service_account.Credentials.from_service_account_info(secret)

    # ------- For accessing gcloud_client_secret locally -------
    # creds = None
    # # The file token.json stores the user's access and refresh tokens.
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # # If there are no valid credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'gcloud_client_secret.json', SCOPES)  # Updated to your file's name
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())
    # ----------------------------------------------------------

    service = build('calendar', 'v3', credentials=creds)

    # Prepare events structure
    events_for_email = {"today": [], "tomorrow": []}
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    # Call the Calendar API for events from today up to tomorrow
    timeMin = today.isoformat() + 'T00:00:00Z'
    timeMax = (tomorrow + datetime.timedelta(days=1)).isoformat() + 'T00:00:00Z'

    print('Getting the upcoming events for today and tomorrow')
    events_result = service.events().list(calendarId='lomvax@gmail.com', timeMin=timeMin,
                                          timeMax=timeMax, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return events_for_email

    # Process and structure events
    for event in events:
        event_date = event['start'].get('dateTime', event['start'].get('date'))
        event_date = datetime.datetime.fromisoformat(event_date).date()

        event_info = {
            "event": event['summary'],
            "start_time": format_event_time(event['start'].get('dateTime', 'All Day'))
            # Add more details as needed
        }

        if event_date == today:
            events_for_email['today'].append(event_info)
        elif event_date == tomorrow:
            events_for_email['tomorrow'].append(event_info)

    return events_for_email


def format_event_time(event_time):
    if event_time == 'All Day':
        return event_time  # No conversion needed for all-day events

    # Directly parse the ISO format string, including its timezone information
    event_dt = datetime.datetime.fromisoformat(event_time)

    # Convert to local time zone, e.g., 'Asia/Tbilisi'
    local_tz = ZoneInfo('Asia/Tbilisi')
    local_dt = event_dt.astimezone(local_tz)

    # Format the datetime object as a string, e.g., '4 PM'
    formatted_time = local_dt.strftime('%-I %p')
    return formatted_time


if __name__ == '__main__':
    events_for_email = fetch_calendar_events()
    # Example output
    print(events_for_email)
