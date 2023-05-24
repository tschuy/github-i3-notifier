GitHub Notifications in i3
==========================

Get GitHub notifications on your i3 status bar.

How-to
------

1) Run ``notification.py`` in the background on i3 load.

To do this, add an ``exec`` command to your i3 config:

```
# ~/.i3/config
exec --no-startup-id /path/to/notification.py &
```

2) Create a file `~/.github-notifications-token` containing a GitHub API token.

To get a token, visit the [GitHub settings](https://github.com/settings/tokens).

You can also set the ``GH_NOTIFICATION_FILE`` that will be used to track whether
you have notifications, and the ``GH_NOTIFICATION_INTERVAL`` between checking
for notifications (default: 60 seconds).

3) Make ``i3status`` read the github notification count file.

Add a ``read_file`` section to your ``~/.i3status.conf`` that reads the contents of
watches for updates to the notification count file (default: ``~/.ghn``):

```
# ~/.i3status.conf

order += "read_file github"
...
read_file github {
        path = "/home/<user>/.ghn"
        format = "  %content "
}
```

The `.ghn` file will contain the count of unread github notifications.

4) Reload i3.

You may need to log out and back in for the environment variable to be properly
set.
