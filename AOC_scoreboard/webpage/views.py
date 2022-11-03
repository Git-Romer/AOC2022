from django.shortcuts import render
import requests, datetime
from bs4 import BeautifulSoup
# Importing Table
from scoreboard.models import jsoncrawler

# Create your views here.

def index(request):
    # Crawling the AOC calendar from the AOC website
    url = 'https://adventofcode.com/2022'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    calendar = soup.main
    for a in calendar.find_all('a'):
        a['href'] = 'https://adventofcode.com' + a['href']
        a['target'] = '_blank'
    context = {'calendar': str(calendar)}
    return render(request, 'index.html', context)

def bongocat(request):
    return render(request, 'bongo_cat.html', {})

def scoreboard(request):
    data = jsoncrawler.objects.all().order_by('-stars')
    podium = {}
    for podiums in range(3):
        if len(data) >= podiums:
            if not data.order_by('-stars', 'name').values('stars')[podiums].get('stars') == 0:
                podium[podiums] = data.order_by('-stars', 'name')[podiums]
            else:
                podium[podiums] = ""
        else:
            podium[podiums] = ""

    startdate = datetime.date(datetime.datetime.now().year, 12, 1)
    enddate = datetime.date(datetime.datetime.now().year, 12, 25)
    if datetime.datetime.now().date() < startdate:
        daycounter = "Challenge has not started yet"
    elif datetime.datetime.now().date() > enddate:
        daycounter = "Challenge has ended"
    else:
        daycounter = "Day " + str(datetime.datetime.now().day) + " of 25"

    context = {
        'data': data,
        'best_user': podium[0],
        'snd_best_user': podium[1],
        'thrd_best_user': podium[2],
        'daycounter': daycounter,
    }
    return render(request, 'scoreboard.html', context)