import tweepy 
from secrets import *
import json 
import requests

# create OAuth handler instance 
# used for authenticating requests 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN) 

# construct an API instance 
api = tweepy.API(auth) 

# using Alpha Vantage to get stock prices 
# api endpoint
URL = "https://www.alphavantage.co/query" 

# a function that uses the googlefinance api to get a stock price 
def get_price(symbol):
    price = -1
    function = "GLOBAL_QUOTE" 
    interval = "60min"
    PARAMS = {
        "function":function,
        "symbol":symbol,
        "apikey":AV_KEY
    }
    try:
        r = requests.get(url = URL, params = PARAMS)
        data = r.json() 
        price = data["Global Quote"]["05. price"]
    except Exception as e:
        print(e)  
    return price 

# a function responsible for responding to a tweet when the bot is summoned 
def tweet_response(text, username, status_id):
    new_message = "@" + username + " Call this bot by tweeting at it with a stock symbol!"  
    tokens = text.split(" ")
    if len(tokens) == 2:
        symbol = tokens[1] 
        price = get_price(symbol.upper()) 
        if price != -1:
            new_message = "@" + username + " " + symbol + " : $" + price
    elif len(tokens) > 2:
        new_message = "@" + username + " Sorry! I can only do one symbol at a time right now!"
    api.update_status(new_message, status_id)

# a class that inherits from StreamListener
class BotStreamer(tweepy.StreamListener):

    def on_status(self, status): 
        username = status.user.screen_name 
        status_id = status.id 
        tweet_response(status.text, username, status_id) 


myStreamListener = BotStreamer() 

"""I want to test the get price method"""
#print(get_price(""))

# construct the stream instance
stream = tweepy.Stream(auth, myStreamListener) 

# filter tweets to ones at the desired username

stream.filter(track=[USERNAME]) 


