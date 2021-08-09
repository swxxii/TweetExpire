#! /bin/python3
import tweepy
from datetime import datetime, timedelta, timezone

##########################################################################
# CONFIGURATION
##########################################################################

# Your twitter handle
username = ""

# Delete tweets once they are this many days old
delete_after = 180

# ID's of protected tweets to keep
protected = [1234567890987654321, 987654321234567890]

# Set this to True to print skipped tweets to stdout
verbose = False

# Twitter API info. Register an app at https://developer.twitter.com/en/apps
api_key = ""
api_secret = ""
access_token_key = ""
access_token_secret = ""

##########################################################################
# MAIN SCRIPT
##########################################################################

print("[ INIT ] TweetExpire script started for @{:s}.".format(username))
print("[ INIT ] About to delete tweets older than {:d} days.".format(
    delete_after))


def deleter(tw, idNo):
    if tw.user.screen_name != username:
        if tw.retweeted == True:
            api.unretweet(idNo)
    else:
        api.destroy_status(idNo)


def clean(text):
    # normalise whitespace
    text = text.replace("\r\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    # strip non-ascii chars
    return ''.join([i if ord(i) < 128 else ' ' for i in text])


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

count = 0
dels = 0
unrt = 0

for tw in tweepy.Cursor(api.user_timeline, id=username).items():
    count += 1
    text = clean(tw.text)[:80] + "..."
    age = (datetime.now() - tw.created_at).days
    sage = "("+str(age)+") "
    if tw.id in protected:
        if verbose:
            print("[ KEEP ] " + tw.created_at.strftime("%Y-%m-%d ") + sage + text)
    if age >= delete_after:
        print("[DELETE] " + tw.created_at.strftime("%Y-%m-%d ") + sage + text)
        deleter(tw, tw.id)
        dels += 1
    else:
        if verbose:
            print("[ SKIP ] "+tw.created_at.strftime("%Y-%m-%d ") + sage + text)

print("[ DONE ] Processed {:d} tweets: {:d} deleted.".format(
    count, dels))
