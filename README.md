# Morning Pages

Computational assistance in establishing daily preparation and reflection habits.

Initiates two CRON jobs that will bring up Morning Pages (at 6AM)
and Evening Pages (at 9PM). These writing prompts ask you to answer a
few short predefined questions. Completing them can help to reflect
and focus on your aims.

Evening Pages now include the [MIT (most important task)](https://github.com/martin-martin/time-mgmt) for the coming day
and open up for revisit in the morning.

Each exercises takes less than 5 minutes.

Install the dependencies from `requirements.txt` and run `cron_pages.py` (Python 3)
to register the jobs in your crontab.

Have fun! :)

## Note

In order for CRON to run, your computer needs to be switched on. You can adapt the
times easily in `cron_pages.py` in the following lines to fit your personal schedule:

```
m_job.hour.on(6)   # <- change for different morning time
e_job.hour.on(21)  # <- change for different evening time
```

## UPDATE: `.plist`

Using `.plist` files on MacOS allows to schedule tasks that run **also later**, e.g.
in case the computer was asleep at the scheduled time.

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
