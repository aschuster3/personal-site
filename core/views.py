from core.models import EssayPost

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    post = EssayPost.objects.latest('time_stamp')

    context = {'post': post}
    return render(request, 'index.html', context)
