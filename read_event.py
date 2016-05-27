from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '-07:00'      # PDT/MST/GMT-7
EVENT = {
    'summary': 'Dinner with friends',
    'start':  {'dateTime': '2015-09-15T19:00:00%s' % GMT_OFF},
    'end':    {'dateTime': '2015-09-15T22:00:00%s' % GMT_OFF},
    'attendees': [
        {'email': 'friend1@example.com'},
        {'email': 'friend2@example.com'},
    ],
}

event = CAL.calendars().get(calendarId='primary').execute()

page_token = None
total_minutes = 0
while True:
    events = CAL.events().list(calendarId='primary', pageToken=page_token).execute()
    for event in events['items']:
        print(event)
        try:
            if 'chris' in event['summary'].lower():
                print(event[''])
            print(event['summary'])
        except:
            print("NO SUMMARY")
    page_token = events.get('nextPageToken')
    if not page_token:
        break
