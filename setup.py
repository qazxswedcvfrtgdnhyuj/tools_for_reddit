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
            'scrub_comments = scrub_comments.__main__:main',
            'auto_reply = auto_reply.__main__:main',
        ]
    }
)
