from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scoreboard_updater import scoreboard_api
import socket

def start():
    if socket.gethostbyname(socket.gethostname()) == '127.0.0.1':
        print(f"Server launched on {socket.gethostbyname(socket.gethostname())}\nReocurring scoreboard update will not be executed!")
    else:
        scheduler = BackgroundScheduler()
        scheduler.add_job(scoreboard_api.update, 'interval', minutes=15)
        scheduler.start()