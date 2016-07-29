from flask import Flask, request
import praw
import webbrowser

import json
import logging
import sys

app = Flask('scrub_comments')

CLIENT_ID = sys.argv[1]
CLIENT_SECRET = sys.argv[2]
REDIRECT_URI = sys.argv[3]

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
    reddit_client = praw.Reddit('Testing a comment scrubbing app.')

    reddit_client.set_oauth_app_info(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
    )
    auth_url = reddit_client.get_authorize_url(
        'scrub_comments',
        'identity read edit history',
        refreshable=True
    )
    webbrowser.open(auth_url)

    app.run(debug=False, port=30040)

    with open('.access_code', 'r') as auth_file:
        code = ''.join(auth_file.readlines()).strip()

    access_info = reddit_client.get_access_information(code)
    reddit_client.set_access_credentials(**access_info)
    user = reddit_client.user

    comments = ['foo']
    while comments:
        comments = user.get_comments(limit=1000)
        if len(list(comments)) == 0:
            print("No more comments to delete, exiting!")
            break
        for comment in comments:
            comment.edit('foo')
            comment.delete()
            print("Comment {} deleted.".format(comment.fullname))
