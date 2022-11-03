from django.shortcuts import render
from django.db.models.functions import Lower
import requests, datetime, numpy as np, seaborn as sns
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

def scoreboard(request):
    data = jsoncrawler.objects.all()
    podium = {}
    for podiums in range(3):
        if len(data) >= podiums:
            if not data.order_by('-stars', Lower('name')).values('stars')[podiums].get('stars') == 0:
                podium[podiums] = data.order_by('-stars', Lower('name'))[podiums]
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

def stats(request):
    def colorize(x):
        randcolor = []
        color_list_hex = sns.color_palette("pastel", x).as_hex()
        for hex in color_list_hex:
            randcolor.append(list(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
        return randcolor

    def randomdata():
        randdata = sorted(list(np.random.choice(range(50), size=25)))
        randdata[0] = 0
        return randdata
    def randomday():
        randday = list(range(np.random.choice(range(2,25))))
        return randday

    data = jsoncrawler.objects.all()
    
    if datetime.datetime.now().date() >= datetime.date(datetime.datetime.now().year, 12, 1) and datetime.datetime.now().date() <= datetime.date(datetime.datetime.now().year, 12, 25):
        max_day = datetime.datetime.now().day
        max_stars = 2 * max_day
    else:
        max_day = 0
        max_stars = 0

    dataset = ""
    colorpalette = colorize(len(data))
    for i, user in enumerate(data.order_by(Lower('name'))):
        dataset = dataset + \
        f"""
        {{
            label: "{user.name}",
            backgroundColor: 'rgb({', '.join(map(str, colorpalette[i]))})',
            borderColor: 'rgb({', '.join(map(str, colorpalette[i]))})',
            data: {randomdata()},
            tension: 0.2,
        }},"""

    context = {
        "dataset": dataset,
        "randomday": randomday(),
        "max_day": max_day,
        "max_stars": max_stars,
    }
    return render(request, 'stats.html', context)

def bongocat(request):
    return render(request, 'bongo_cat.html', {})