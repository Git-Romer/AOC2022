from django.shortcuts import render
import requests
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
    data = jsoncrawler.objects.all().order_by('stars')
    if len(data.order_by('stars')) > 0:
        best_user = data.order_by('stars')[0]
    else:
        best_user = ""
    if len(data.order_by('stars')) > 1:
        snd_best_user = data.order_by('stars')[1]
    else:
        snd_best_user = ""
    if len(data.order_by('stars')) > 2:
        thrd_best_user = data.order_by('stars')[2]
    else:
        thrd_best_user = ""
    # users = jsoncrawler.objects.values_list('name', flat=True)
    context = {
        'data': data,
        'best_user': best_user,
        'snd_best_user': snd_best_user,
        'thrd_best_user': thrd_best_user,
    }
    return render(request, 'scoreboard.html', context)