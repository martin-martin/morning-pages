# Morning Pages

Computational assistance in establishing daily preparation and reflection habits.

Initiates two cron jobs that will bring up Morning Pages (at 7AM)
and Evening Pages (at 10PM) that prompt you to answer to short pre-defined
questions.

Each exercises takes less than 5 minutes.

Install the dependencies from `requirements.txt` and run `pages.py` (Python 3)
to register the jobs in your crontab.

Have fun! :)

---

## Note

In order for cron to run, your compter needs to be switched on. You can adapt the
times easily in `pages.py` in the following lines to fit your personal schedule:

```
m_job.hour.on(6)   # <- change for different morning time
e_job.hour.on(21)  # <- change for different evening time
```

---

## Resources

- http://stackabuse.com/scheduling-jobs-with-python-crontab/
- https://tim.blog/2017/07/19/morning-routines-and-strategies/
