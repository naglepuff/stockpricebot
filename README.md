# stockpricebot

A simple twitter bot written in python using the tweepy library. 

The bot watches for tweets containing the string "@stockpricebot" 

Once the bot finds one, it breaks down the tweet into tokens based on the ' ' character (space). 

Right now it can only handle a request for one stock symbol. 

And example tweet it will respond to is "@stockpricebot GOOG" or "@stockpricebot goog"

The bot takes advantage of the Alpha Vantage API to get stock prices. 

Future updates include:

1. Support for multiple stock symbols. 
2. Support for reporting change in stock value over a stated time. 
3. Support for returning images of graphs of a stocks behavior over a given time.
