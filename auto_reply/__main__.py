from flask import Flask, request
import praw
import webbrowser

import json
import logging
import sys
import time

app = Flask('auto_reply')

CLIENT_ID = sys.argv[1]
CLIENT_SECRET = sys.argv[2]
REDIRECT_URI = sys.argv[3]
BAD_GUY_NAME = sys.argv[4]
REPLY_CONTENT = sys.argv[5]

werkzeug_log = logging.getLogger('werkzeug')
werkzeug_log.setLevel(logging.ERROR)

@app.route('/auth_token')
def set_auth_token():
    state = request.args.get('state', '')
    code = request.args.get('code', '')

    with open('.access_code', 'w') as auth_data:
        auth_data.write(code)

    request.environ['werkzeug.server.shutdown']()

    return 'You can close me whenever you like.'

def main():
    reddit_client = praw.Reddit('Reddit tools app.')

    reddit_client.set_oauth_app_info(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
    )
    auth_url = reddit_client.get_authorize_url(
        'auto_reply',
        'identity read edit history privatemessages',
        refreshable=True
    )
    webbrowser.open(auth_url)

    app.run(debug=False, port=30040)

    with open('.access_code', 'r') as auth_file:
        code = ''.join(auth_file.readlines()).strip()

    access_info = reddit_client.get_access_information(code)
    reddit_client.set_access_credentials(**access_info)
    user = reddit_client.user

    while True:
        print("Refreshing access tokens.")
        updated_access_info = reddit_client.refresh_access_information()
        reddit_client.set_access_credentials(**updated_access_info)
        for comment in reddit_client.get_unread(limit=100):
            if str(comment.author) == str(BAD_GUY_NAME):
                print("Found evil comment, replying.".format())
                comment.reply(REPLY_CONTENT)
                comment.mark_as_read()
        print("Sleeping for 1 minute.")
        time.sleep(60)
