# TweetExpire

A python script to delete your tweets once they reach a certain age (number of days old). I run it as a cron job every night.

The Twitter API only returns max 3200 tweets. This script may not be suitable if you want to delete really old tweets past this limit. For that, try [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.

## Getting started/basic Linux install

1. [Register a Twitter App](https://developer.twitter.com/en/apps) and get the API keys.
2. Install Python and tweepy. I use Python 3.   
    e.g. `pip3 install tweepy`
3. Enter configuration info in the script.
4. Run the script `./TweetExpire.py`

## Synology NAS install

1. Enable SSH access via DSM

2. Install the Python 3 package via DSM

3. To use pip, create a Python virtual environment. \([credit](https://stackoverflow.com/questions/47649902/installing-pip-on-a-dsm-synology)).
   
   ```
   admin@server:~$ python3 -m venv env
   admin@server:~$ . env/bin/activate
   (env) admin@server:~$ pip install --upgrade pip
   ```
   
4. Install Tweepy  `pip install tweepy`

5. Put the configured **TweetExpire.py** script somewhere on your NAS

6. Create a script to run the script inside your virtual Python (use script path from your own setup)
   
   ```bash
   #!/bin/bash
   . env/bin/activate
   python /volume1/configs/scripts/TweetExpire.py
   ```

7. If it works, create a scheduled task in Synology DSM to run the script as admin user.

## Acknowledgements

Based on [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.
