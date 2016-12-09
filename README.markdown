# Secret Santa!

Secret Santa is a simple Python script that sends emails to participants in a "Secret Santa" style gift exchange pool. The participants in the pool are defined in a Google Spreadsheet so the participants can add, remove, or edit their own email address and other preferences. :)

# Configure

In order to use this tool, please first create a spreadsheet in Google Drive. The spreadshet will need to have at least two columns, with the exact headings:

 1. `Name`
 1. `Email`

An optional third column can be added and will be treated as exceptions. For example, if you would like people to avoid picking their significant other or their immediate family members, your participants should type that person's (those people's) name(s) in this third column. The title of the third column is up to you, and feel free to leave it blank if this does not apply to your group.

Once your participants have all filled out their information in your spreadsheet, you are ready to [run the code](#running)!

Please note that if you choose the email, you will be prompted to enter your email and password, which will be used to         (securely) send emails through your email. If you are using gmail, you will have to turn on the setting to allow less secura eapps.

See [an example Google Sheet here](https://docs.google.com/spreadsheets/d/17c6b5twbL0lRo1aID6nd3nnNGjsBfNq6Q5GAVlQ3B4s/edit).

# Installing

```sh
git clone https://github.com/steph-rage/Secret_santa.git # Download the code.
cd Secret_santa                                          # Change to the download directory.
# If you want a temporary install, be sure you have virtualenv
virtualenv santa                                         # Create a virtual environment.
source ./santa/bin/activate                              # Activate the virtual environment.
pip install -r requirements.txt                          # Install dependencies.
```

Next, you will need to obtain OAuth 2.0 client credentials from your own Google Account's Developer Console and save these credentials in a file called `client_secrets.json`.

**Do this:**

1. Go to the [Google Developers API Console](https://console.developers.google.com/).
1. Create a new Project.
1. Obtain an OAuth client ID from [the "Credentials" section](https://console.developers.google.com/apis/credentials)
1. Download the JSON file for the new credentials, and save the file as `client_secrets.json` in the same folder as this file is in.

See the following Google Developer guides for more information:

* [Client Secrets | API Client Library for Python | Google Developers](https://developers.google.com/api-client-library/python/guide/aaa_client_secrets)
* [Using OAuth 2.0 to Access Google APIs | Google Identity Platform | Google Developers](https://developers.google.com/identity/protocols/OAuth2?csw=1#CS)

# Running

After [installing](#installing) the program, simply run it as so:

```sh
python Secret_santa_v2.py
```
