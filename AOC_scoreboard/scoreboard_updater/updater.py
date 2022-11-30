from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scoreboard_updater import scoreboard_api
import socket
from django.conf import settings

def start():
    if settings.DEBUG:
        print(f"Server launched on {socket.gethostbyname(socket.gethostname())} and Debug mode is on\nReocurring scoreboard update will not be executed!")
    else:
        scheduler = BackgroundScheduler()
        scheduler.add_job(scoreboard_api.main, 'interval', minutes=30)
        scheduler.start()