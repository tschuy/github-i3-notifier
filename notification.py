#!/usr/bin/env python

import json
import requests
import os
import time
import sys
import pathlib

from notifypy import Notify

HOME = os.environ.get("HOME")

with open(f"{HOME}/.github-notifications-token", "r") as file:
    TOKEN = file.read().rstrip()

FILE = os.environ.get("GH_NOTIFICATION_FILE", f"{HOME}/.ghn")
INTERVAL = int(os.environ.get("GH_NOTIFICATION_INTERVAL", 60))

prev_notification_count = None

notification = Notify(
    default_notification_title="GitHub Notifications",
    default_application_name="GitHub Notifier",
    default_notification_icon=f"{pathlib.Path(__file__).parent.resolve()}/github-mark_120.png",
)

while True:
    response = requests.get(
        f"https://api.github.com/notifications",
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        },
    )
    notification_count = len(response.json())
    with open(FILE, "w") as f:
        f.write(f"{notification_count}")

    if prev_notification_count is None or prev_notification_count < notification_count:
        notification.message = f"{notification_count} unread notifications."
        notification.send()

    prev_notification_count = notification_count

    time.sleep(INTERVAL)
