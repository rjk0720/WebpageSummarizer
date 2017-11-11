#!/usr/bin/env python
# main.py

from keys import keys
from summarizer import summarize

url = "https://www.theverge.com/2017/11/10/16631774/twitter-verification-kessler-milo-abuse"
summary,chars = summarize(url)
print(summary)
print(str(chars) + " characters")

# from twitter import *
# import tweepy
#
# t = Twitter(auth=OAuth(keys['access_token'], keys['access_token_secret'], keys['consumer_key'], keys['consumer_secret']))
#
# auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
# auth.set_access_token(keys['access_token'], keys['access_token_secret'])
# api = tweepy.API(auth)

# tweets = api.search(q="Hello World!")
#
# for s in tweets:
#     for i in t:
#         if i == s.text:
#             sn = s.user.screen_name
#             m = "@%s Hello!" % (sn)
#             s = api.update_status(m, s.id)