import datetime
import json
import logging
import os
import smtplib
import time
from uuid import uuid4

import requests
from dotenv import load_dotenv

load_dotenv('login.env')

# Configuration
# [Warning]: This is the only spot for configuration; the rest is modify at your own risk!

LOG_LEVEL = logging.INFO  # Log level for terminal output
# [Info]: Set this to logging.INFO to view assignments and status updates in the terminal
# [Info]: Set this to logging.DEBUG to view networking logs
# [Info]: Set this to logging.ERROR or logging.CRITICAL higher to hide messages

SHOW_SUBMITTED = False  # Whether or not submitted assignments are checked
SHOW_LATE = True  # Whether or not late assignments are checked
SHOW_SUBMISSIONS = True  # Whether or not the number of submissions is displayed

SEND_MESSAGE = False  # Whether or not a email reminder is sent
# [Info]: Specify the email address to send in the logins.env, see README.txt for more info
# [Info]: This can also be set up for texting, see README.txt for more info

HOURS = 2  # The number of hours into the future to check
DAYS = 2  # The number of days into the future to check
# [Info]: This will also be able to check items before this date

DELAY = 1800  # The number of seconds delay between checking
# [Warning]: Refrain from making the delay too small as to not overload the Schoology API

# End Configuration

logging.basicConfig(level=LOG_LEVEL)


def get_headers():
    return {
        'Authorization': generate_auth(),
        'Accept': 'application/json',
        'Host': 'api.schoology.com',
        'Content-Type': 'application/json'
    }


def generate_auth():
    auth = 'OAuth realm="Schoology API",'
    auth += f'oauth_consumer_key="{os.getenv("CONSUMER_KEY")}",'
    auth += 'oauth_token="",'
    auth += f'oauth_nonce="{uuid4()}",'
    auth += f'oauth_timestamp="{int(time.time())}",'
    auth += f'oauth_signature_method="PLAINTEXT",'
    auth += 'oauth_version="1.0",'
    auth += f'oauth_signature="{os.getenv("consumer_secret") + "%26"}"'
    return auth


def send_message(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.getenv('USER'), os.getenv('PWD'))
    server.sendmail(os.getenv('USER'), os.getenv('EMAIL'), message)
    server.quit()


def check_sections():
    url = f'https://api.schoology.com/v1/users/{os.getenv("USER_ID")}/sections'
    r = requests.get(url, headers=get_headers())
    json_data = json.loads(r.text)
    for section in json_data['section']:
        check_assignments(section)


def check_assignments(section):
    url = f'https://api.schoology.com/v1/sections/{section["id"]}/assignments'
    r = requests.get(url, headers=get_headers())
    json_data = json.loads(r.text)
    for assignment in json_data['assignment']:
        if assignment['type'] == "assignment":
            submissions = check_submissions(section, assignment["grade_item_id"])
            if SHOW_SUBMITTED or submissions == 0:
                if len(assignment['due']) > 0:
                    date_time = datetime.datetime.fromisoformat(assignment['due'].replace(' ', 'T'))
                    delta = date_time - datetime.datetime.now()
                    if (SHOW_LATE or delta.total_seconds() > 0) and delta.total_seconds() < 3600 * HOURS + 86400 * DAYS:
                        title, course = assignment["title"], section["course_title"]
                        message = f'"{title}" from "{course}" is due in {delta}'
                        if SHOW_SUBMISSIONS:
                            message += f', submissions: {submissions}'
                        logging.info(message)
                        if SEND_MESSAGE:
                            send_message(message)


def check_submissions(section, grade_item_id):
    url = f'https://api.schoology.com/v1/sections/{section["id"]}/submissions/{grade_item_id}/{os.getenv("USER_ID")}'
    r = requests.get(url, headers=get_headers())
    json_data = json.loads(r.text)
    return len(json_data['revision'])


if __name__ == '__main__':
    logging.info('Started Program')
    while True:
        logging.info(f'Checking assignments... ({datetime.datetime.now()})')
        check_sections()
        logging.info(f'Checked Assignments ({datetime.datetime.now()})')
        time.sleep(DELAY)
