#!/usr/bin/python2
import json
import urllib2
import os
import time
import sys

TOKEN = os.environ.get('GH_NOTIFICATION_TOKEN')
if not TOKEN:
    print "Set GH_NOTIFICATION_TOKEN env var to a GitHub API token!"
    print "Generate a token at https://github.com/settings/tokens"
    sys.exit(1)

FILE = os.environ.get('GH_NOTIFICATION_FILE', '~/.ghn')
INTERVAL = int(os.environ.get('GH_NOTIFICATION_INTERVAL', 60))

while True:
    response = urllib2.urlopen('https://api.github.com/notifications?access_token={}'.format(TOKEN))
    notifications = json.load(response)
    if notifications:
        open(FILE, 'a').close()
    else:
        try:
            os.remove(FILE)
        except OSError:
            pass
    time.sleep(INTERVAL)
