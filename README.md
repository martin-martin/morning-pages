# Morning Pages

Computational assistance in establishing daily preparation and reflection habits.

Initiates two cron jobs that will bring up Morning Pages (at 7AM)
and Evening Pages (at 10PM) that prompt you to answer to short pre-defined
questions.

Each exercises takes less than 5 minutes.

Install the dependencies from `requirements.txt` and run `cron_pages.py` (Python 3)
to register the jobs in your crontab.

Have fun! :)

# Note

In order for cron to run, your compter needs to be switched on. You can adapt the
times easily in `cron_pages.py` in the following lines to fit your personal schedule:

```
m_job.hour.on(6)   # <- change for different morning time
e_job.hour.on(21)  # <- change for different evening time
```

## UPDATE: `.plist`

Using `.plist` files on MacOS allows to schedule tasks that run **also later**, e.g.
in case the computer was asleep or switched off at the scheduled time.

The `.plist` files need to be loaded in order to work, and the **working directory**
needs to be adapted for your specific path. Change the `<string>` part of this:

```
    <key>WorkingDirectory</key>
        <string>/Users/martin/Documents/projects/daily/</string>
```

to the path where you clone this repository to.
(Also the `<string>` in `<key>StandardErrorPath</key>` needs to be set to the
    same directory to receive error logs)

For easiest use of the `.plist` job, I would suggest to move both `.plist` files
into your `/Users/<yourUserName>/Library/LaunchAgents/` folder (create it if it doesn't
    yet exist). All `.plist`s in this folder get automatically loaded during system startup.

---

## Resources

- http://stackabuse.com/scheduling-jobs-with-python-crontab/
- https://tim.blog/2017/07/19/morning-routines-and-strategies/
- https://nathangrigg.com/2012/07/schedule-jobs-using-launchd
- https://alvinalexander.com/mac-os-x/launchd-plist-examples-startinterval-startcalendarinterval
