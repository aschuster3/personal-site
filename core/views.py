from core.models import EssayPost

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    essay = EssayPost.objects.latest('time_stamp')

    return render(request, 'index.html')
