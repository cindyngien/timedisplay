from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    context = {
    "time":datetime.datetime.now()
    }
    return render(request,'time_display/index.html', context)
