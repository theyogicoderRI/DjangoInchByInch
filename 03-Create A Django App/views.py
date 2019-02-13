
from django.shortcuts import render
from datetime import datetime


def home(request):
    current_user = "Mable Marbles"
    return render(request, 'home.html',
        {'date': datetime.now(),'login' : current_user})




