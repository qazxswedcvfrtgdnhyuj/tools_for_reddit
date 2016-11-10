import click

from reddit_tools.utils import get_client


@click.command()
@click.option('--replacement-text', '-r', default='Foo.')
def scrub_comments(replacement_text):
    reddit_client = get_client()
    print('Reddit client created.')
    user = reddit_client.user
    print('User fetched.')

    comments = [replacement_text]

    while len(set(comments)) > 0:
        print('Fetching comments.')
        comments = user.get_comments(limit=1000)
        for comment in comments:
            comment.edit(replacement_text)
            comment.delete()
            print('Comment {} deleted.'.format(comment.fullname))


def main():
    scrub_comments()
