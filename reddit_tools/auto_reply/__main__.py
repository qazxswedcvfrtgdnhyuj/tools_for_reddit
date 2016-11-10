import click
import time
from reddit_tools.utils import get_client


@click.command()
@click.option('--reply-user', '-u')
@click.option('--reply-content', '-c')
def auto_reply(reply_user, reply_content):
    while True:
        print("Searching recent comments for user {}.")
        for comment in get_client().get_unread(limit=100):
            if str(comment.author) == str(reply_user):
                print("\tFound comment, replying.")
                comment.reply(reply_content)
                comment.mark_as_read()
        print("Sleeping for 1 minute.")
        time.sleep(60)


def main():
    auto_reply()
