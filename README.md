#Tools for Reddit

##Setup
* Uses [OAuth2Util](https://github.com/SmBe19/praw-OAuth2Util/blob/master/OAuth2Util/README.md#config), these tools need an `oauth.ini` file in the base directory in order to function.  
* OAuth2Util configuration will also require you register your own [Reddit script app](https://github.com/reddit/reddit/wiki/OAuth2).
```
virtualenv env -p python3.5 && source env/bin/activate
pip install -r requirements.txt
python setup.py install
```

##Commands

* `scrub_comments <REPLACEMENT_TEXT>`
* `auto_reply <USER_NAME> <REPLY>`

#Planned Commands

* `clone_user`
