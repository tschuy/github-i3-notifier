#!/usr/bin/env python

import json
import requests
import os
import time
import sys

HOME = os.environ.get("HOME")

with open(f"{HOME}/.github-notifications-token", "r") as file:
    TOKEN = file.read().rstrip()

print(f"'{TOKEN}'")

FILE = os.environ.get("GH_NOTIFICATION_FILE", f"{HOME}/.ghn")
INTERVAL = int(os.environ.get("GH_NOTIFICATION_INTERVAL", 60))

while True:
    response = requests.get(
        f"https://api.github.com/notifications",
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        },
    )
    notifications = response.json()
    print(f"notification count: {len(notifications)}")
    with open(FILE, "w") as f:
        f.write(f"{len(notifications)}")
    time.sleep(INTERVAL)
