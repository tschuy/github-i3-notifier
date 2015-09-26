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

2) Set ``GH_NOTIFICATION_TOKEN`` environment variable to a GitHub API token.

To get a token, visit the [GitHub settings](https://github.com/settings/tokens).

To make sure this variable is set before the notification script is run, add
it to your ``~/.profile`` file.

You can also set the ``GH_NOTIFICATION_FILE`` that will be used to track whether
you have notifications, and the ``GH_NOTIFICATION_INTERVAL`` between checking
for notifications (default: 60 seconds).

3) Make ``i3status`` watch for the GitHub notifications file.

add a ``run_watch`` to your ``~/.i3status.conf`` that watches for the
notification file (default: ``~/.ghn``):

```
# ~/.i3status.conf

order += "run_watch GH"
...
run_watch GH {
        pidfile = "/home/tschuy/.ghn"
}
```

Whenever the file exists, ``i3status`` will report ``Yes``, and likewise, when
the file does not exist, it will report ``No``.

4) Reload i3.

You may need to log out and back in for the environment variable to be properly
set.
