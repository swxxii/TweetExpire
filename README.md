# TweetExpire

A python script to delete your tweets once they reach a certain age (number of days old). I run it as a cron job every night.

The Twitter API only returns max 3200 tweets. This script may not be suitable if you want to delete really old tweets past this limit. For that, try [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.

## Basic Linux install

1. [Register a Twitter App](https://developer.twitter.com/en/apps) and get the API keys.
2. Install Python and tweepy. I use Python 3.   
    e.g. `pip3 install tweepy`
3. Enter configuration info in the script.
4. Run the script `./TweetExpire.py`

## Synology NAS install

1. Install the Python 3 package via DSM. (3.8.2 used)

2. Enable SSH access via DSM and log in as `admin`

3. Invoke pip using this command to install the tweepy module

    ```
    admin@server:~$ /volume1/\@appstore/py3k/usr/local/bin/pip3 install tweepy
    ```

5. Put the configured `TweetExpire.py` script somewhere on your NAS.

6. Test it manually from the shell to make sure it works.
    ```
    admin@server:~$ python3 /volume1/configs/scripts/TweetExpire.py
    ```
6. Create a cron job (scheduled task) in Synology DSM with the above command to run as `admin` user. 

## Acknowledgements

Based on [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.
