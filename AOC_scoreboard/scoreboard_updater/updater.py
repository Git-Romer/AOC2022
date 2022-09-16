from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scoreboard_updater import scoreboard_api

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scoreboard_api.update, 'interval', minutes=15)
    scheduler.start()