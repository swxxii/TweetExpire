# TweetExpire

A python script to delete your tweets once they reach a certain age (number of days old). I run it as a cron job every night.

The Twitter API only returns max 3200 tweets. This script may not be suitable if you want to delete really old tweets past this limit. For that, try [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.

## Basic Linux install

1. [Register a Twitter App](https://developer.twitter.com/en/apps) and get the API keys.
2. Assume you have installed Python and pip. 
3. Install tweepy package  `pip3 install tweepy`
3. Enter config info in the script.
4. Run the script `./TweetExpire.py`

## Synology NAS install

1. As of DSM 7, Python 3 is bundled so no need to install it.
2. Enable SSH access and log in with an account (e.g. `nasadmin`)
4. Install pip `sudo python3 -m ensurepip`
5. Install tweepy package  `pip3 install tweepy`
6. Enter your config info in the script.
7. Put the `TweetExpire.py` script somewhere on your NAS.
6. Test it manually from the shell to make sure it works.
    ```
    nasadmin@server:~$ python /volume1/configs/scripts/TweetExpire.py
    ```
6. Create a cron job (scheduled task) in Synology DSM with the above command to run as the same user - `nasadmin` you used to setup Python. 

## Acknowledgements

Based on [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.
