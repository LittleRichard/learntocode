import json
import logging
import requests
import smtplib  # SMTP library - interact with an email server

# python builtins include email libraries
# often you don't need an entire library, so importing
# just a couple pieces is a good idea:
# from <library or package within library> import <something>
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("""
This script uses two different APIs;
1. A URL shortener so a huge URL looks smaller.
   This also obscures the link a little bit, which
   can be fun.
2. Not an API in the sense we've been discussing, but
   sending email works in a similar way.  Instead of 
   sending GET/POST requests, you can use libraries
   to deal with the email protocols and send emails
   in just a few lines of code.
""")

# NEVER EVER EVER commit API keys, passwords, etc
# to git; the whole point of git is that it saves
# stuff forever.  Instead, I'll store relevant secrets
# in a file locally and load it into python so it's
# never visible on screen.

# To use this script, you'll need to define your own
# JSON file at this path. Note that you have to enable
# a setting in gmail if you want to let your username/password
# send emails over API (which is why I didn't use my personal email)
SECRETS_FILE = 'data/another_api.json'

# this file should be valid JSON and have all required info, like:
# {
#     "email_user": "maybe",
#     "email_pass": "definitely not",
#     "email_server_url": "smtp.gmail.com:587",
#     "link_to_send": "test4"
# }

with open(SECRETS_FILE) as fh:
    secrets_dict = json.loads(fh.read())

    EMAIL_SERVER_URL = secrets_dict['email_server_url']
    EMAIL_USER = secrets_dict['email_user']
    EMAIL_PASS = secrets_dict['email_pass']

    # this doesn't really need to be a secret,
    # but was convenient to put there so a long
    # string isn't hard-coded in here.
    LINK_TO_SEND = secrets_dict['link_to_send']


def send_email(email_from, email_to, subject, body_text):
    email_to_str = ', '.join(email_to)

    msg = MIMEMultipart()  # MIME is a data format
    msg[u"From"] = email_from
    msg[u"To"] = email_to_str
    msg[u"Subject"] = subject
    msg.preamble = u"learntocode"
    msg.attach(MIMEText(body_text, u'plain'))
    
    print(f'Accessing {EMAIL_SERVER_URL} with credentials')

    # log into the server 
    server = smtplib.SMTP(EMAIL_SERVER_URL)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)

    # once logged in, we can send an email
    print(f'sending email to {email_to}')
    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()


def get_short_link(input_url):
    # the format of this is defined by the API
    payload = {'url': input_url}

    # this API uses 'POST'
    # https://cleanuri.com/docs
    resp = requests.post('https://cleanuri.com/api/v1/shorten',
                         data=payload)
    resp_data_from_json = resp.json()

    # shape of returned data also defined by API
    return resp_data_from_json['result_url']

emails_list = [
    # empty, not going to commit 
    # anyone's personal info to git.
    # Insert your targets here!
]

short_url = get_short_link(LINK_TO_SEND)
print(f'using short URL {short_url}')

body_text = f"""
Click me or I'll feel pretty let down after all my hard work:
{short_url}
"""

if len(emails_list) > 0:
    # you used to be able to spoof emails by specifying your
    # 'From' email address... but this is how phishing works
    # so i'm not surprised google disabled it on their servers.
    send_email('ignored@gmail.com', 
               emails_list,
               'APIs are fun',
               body_text)
else:
    print('no emails in list to send')
