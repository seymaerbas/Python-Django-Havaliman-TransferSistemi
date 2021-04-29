from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting': setting}
    return render(request, 'index.html', context)

def hakkımızda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkımızda'}
    return render(request, 'hakkımızda.html', context)

def referanslarımız(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referanslarımız'}
    return render(request, 'referanslarımız.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context)