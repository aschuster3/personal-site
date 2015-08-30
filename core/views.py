from core.forms import MessageForm
from core.models import EssayPost

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    post = EssayPost.objects.latest('time_stamp')
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'post': post, 'form': form}
    return render(request, 'index.html', context)
