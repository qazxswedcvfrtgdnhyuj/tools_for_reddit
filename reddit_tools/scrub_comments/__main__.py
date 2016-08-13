import time

import click
import praw
import OAuth2Util


@click.command()
@click.option('--replacement-text', '-r', default='Foo.')
def scrub_comments(replacement_text):
    reddit_client = get_client()
    print("Reddit client created.")
    user = reddit_client.user
    print("User fetched.")

    comments = [replacement_text]

    while len(set(comments)) > 0:
        print("Fetching comments.")
        comments = user.get_comments(limit=1000)
        for comment in comments:
            comment.edit(replacement_text)
            comment.delete()
            print("Comment {} deleted.".format(comment.fullname))

def main():
    scrub_comments()


def get_client():
    reddit_client = praw.Reddit("A tool for reddit!")
    oauth = OAuth2Util.OAuth2Util(reddit_client, configfile='oauth.ini')
    oauth.refresh(force=True)

    return reddit_client
