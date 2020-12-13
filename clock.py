import logging
# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import stack_overflow_page
import datetime
# import os
schedule = BlockingScheduler()


def setup_logger():
    # create logger with 'so_fanatic_script'
    logger = logging.getLogger('so_fanatic_script')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('mylog.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)


@schedule.scheduled_job('interval', hours=7)
def access_stack_overflow_page():
    print("clock ticking..")
    print(datetime.datetime.now().time())
    stack_overflow_page.login()


setup_logger()
schedule.start()

if __name__ == "__main__":
    access_stack_overflow_page()
