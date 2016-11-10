from setuptools import setup, find_packages

setup(
    name='reddit_tools',
    version='0.0.0',
    license='WTFPL',
    packages=find_packages('scrub_comments'),
    install_requires=[
        'praw',
        'flask',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'scrub_comments = reddit_tools.scrub_comments.__main__:main',
            'auto_reply = reddit_tools.auto_reply.__main__:main',
        ]
    }
)
