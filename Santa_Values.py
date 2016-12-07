import httplib2
import os

from googleapiclient import discovery, errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


# What permissions to request from the Google API.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# Where to find the client_secrets.json formatted file.
#
# If you don't have this file already, you need to generate one for
# your copy of this app. This is free. The process is:
#
# 1. Go to https://console.developers.google.com/
#
# 2. Create a new Project.
#
# 3. Obtain an OAuth client ID from the "Credentials" section:
#    https://console.developers.google.com/apis/credentials
#
# 4. Download the JSON file for the new credentials, and save
#    the file as `client_secrets.json` in the same folder as
#    this file is in.
#
# See the following Google Developer guides for more information:
#     https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
#     https://developers.google.com/identity/protocols/OAuth2?csw=1#CS
#
CLIENT_SECRETS_FILE = 'client_secrets.json'

# The name of this app that the OAuth authorization flow should show to a user.
APPLICATION_NAME = 'Secret Santa'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():

    global email_or_text
    def get_spreadsheet_Id():
        print("\nTo start, we need the ID for your spreadsheet, which can be found in its URL.\n\nFor example, the spreadsheet located at: https://docs.google.com/spreadsheets/d/17c6b5twbL0lRo1aID6nd3nnNGjsBfNq6Q5GAVlQ3B4s/edit#gid=0\n\nHas the ID: 17c6b5twbL0lRo1aID6nd3nnNGjsBfNq6Q5GAVlQ3B4s\n")
        return input("Please enter the ID of your spreadsheet: ").strip()

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)


    spreadsheetId = get_spreadsheet_Id()
    rangeName = 'Sheet1!A2:D'
    try:
        check_column_1 = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range='Sheet1!A1').execute()
        check_column_2 = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range='Sheet1!B1').execute()
        if check_column_1['values'][0][0].lower() != 'name' or check_column_2['values'][0][0].lower() != ('email'):
            print("The columns in your spreadsheet do not appear to be labeled correctly. Remeber, the first column should be 'Name' and the second column should be 'Email'")
            values = False
        else:
            email_or_text = check_column_2['values'][0][0].lower()
            result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
            values = result.get('values', [])
    except errors.HttpError:
        print("\n----------------------------------------------------------------\nWe could not find an existing spreadsheet with that ID. Please check the ID and try again.")
        get_spreadsheet_Id()

    if not values:
        print('No data found.')
    else:
        return values
            


participants_list = main()
participants = {}
restrictions = []
for person in participants_list:
    try:
        person[2].replace(",", "")
        personal_restrictions = person[2].split(' ')
        personal_restrictions.append(person[0])
        restrictions.append(personal_restrictions)
    except:
        pass
    participants[person[0]] = person[1]



