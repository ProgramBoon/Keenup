import psycopg2
import sys
import os
import datetime
import schedule
sys.path.append(os.getcwd() + '/Keenup.lib')
import database
import cre2
import sne
import time


class ScheduleManager(object):
    _schedtime: int
    def __init__(self):
        p = cre2.XML('ui')
        ScheduleManager.schedtime = int(p.parsingFile("cron", True))

    @staticmethod
    def job():
        sne.Sne._getInfo()
        sne.Sne._toPrint()
        p = database.Database()
        p.insert_data(sne.Sne._ret())
        p.alarm()

    @classmethod
    def run(self):
        schedule.every(ScheduleManager.schedtime).seconds.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(ScheduleManager.schedtime)

