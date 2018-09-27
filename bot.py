"""
The code for the actual twitter bot.
"""

import tweepy 
from secrets import * 

# create OAuth handler instance 
# used for authenticating requests 

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN) 

# construct an API instance 

api = tweepy.API(auth) 