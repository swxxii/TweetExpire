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

3. Upgrade pip inside a local Python environment. This lets you modify Python without affecting the main system installation, which could break stuff \([credit](https://stackoverflow.com/questions/47649902/installing-pip-on-a-dsm-synology)).
   
   ```bash
   admin@server:~$ python3 -m venv env
   admin@server:~$ . env/bin/activate
   (env) admin@server:~$ pip install --upgrade pip
   ```
   
   To set this as default every time the user logs in, make this your  `~/.profile`
   
   ```
   #!/bin/bash
   . env/bin/activate
   ```

4. Install Tweepy  `pip install tweepy`

5. Put the configured **TweetExpire.py** script somewhere on your NAS

6. In the (env) mode, find out the path to your local Python
   
   ```(env) admin@server:/volume1/configs/scripts$ which python
   (env) admin@server:~$ which python
   /volume1/homes/admin/env/bin/python
   ```

7. Run the script manually using the absolute path to Python from last step. 
   
   ```
   /volume1/homes/admin/env/bin/python /volume1/configs/scripts/TweetExpire.py
   ```

8. If it works, create a scheduled task in Synology DSM with the above command, running as admin user (or whatever your preference).

## Acknowledgements

Based on [TweetDeleter](https://github.com/Guerillero/TweetDeleter) by Guerillero.
