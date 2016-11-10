import praw
import OAuth2Util


def get_client():
    reddit_client = praw.Reddit("A tool for reddit!")
    oauth = OAuth2Util.OAuth2Util(reddit_client, configfile='oauth.ini')
    oauth.refresh(force=True)

    return reddit_client
