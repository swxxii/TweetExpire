# TweetExpire

A python script to delete your tweets once they reach a certain age (number of days old). I run it as a cron job every night.

The Twitter API only returns max 3200 tweets. This script may not be suitable if you want to delete really old tweets past this limit. For that, try [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.

## Getting started

1. [Register a Twitter App](https://developer.twitter.com/en/apps) and get the API keys.
2. Install Python and tweepy. I use Python 3.\
    `pip3 install tweepy`
3. Enter configuration info in the script.
4. Run the script `./TweetExpire.py`

## Acknowledgements

Based on [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.
