from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = "HELLO SQL TEAM, VERY GOOD "
    if h < 12:
        msg = msg + "MORNING!!"
    elif h < 16:
        msg = msg + "AFTERNOON"
    elif h < 21:
        msg = msg + "EVENING"
    else:
        msg = msg + "NIGHT"
    return render(request, 'sqlapp/home.html', {'m': msg})


def update_view(request):
    return render(request, 'sqlapp/update.html')

