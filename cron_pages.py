# /usr/local/bin/python3
from crontab import CronTab


# ----------- INITIAL SETUP ----------- #
# NOTE: one-time registers the cron job.
# run again in case you change directory

# initiate crontab object
cron = CronTab(user=True)  # user=True uses current user profile

'''
ALL BASH COMMANDS SPLIT UP

    # grab variables
cwd=`pwd`;d=`date '+%Y_%m_%d'`;

    # grab blank files
morning='$cwd/morning.txt';evening='$cwd/evening.txt';

    # assign new files variables
new_m='$cwd/$d_1.txt';new_e='$cwd/$d_2.txt';

    # create new files from blanks
cp $morning $new_m;cp $evening $new_e;

    # open created files
open $new_m;open $new_e;

'''


# and combined
morning = 'cwd=`pwd`;d=`date "+%Y_%m_%d"`;morning="$cwd/morning.txt";new_m="$cwd/$d-1.txt";cp $morning $new_m;open $new_m;'
evening = 'cwd=`pwd`;d=`date "+%Y_%m_%d"`;evening="$cwd/evening.txt";new_e="$cwd/$d-2.txt";cp $evening $new_e;open $new_e;'

# create and register CRON jobs
m_job = cron.new(command=morning, comment="bring up morning pages")
e_job = cron.new(command=evening, comment="bring up evening pages")
m_job.hour.on(6)
e_job.hour.on(21)
cron.write()
