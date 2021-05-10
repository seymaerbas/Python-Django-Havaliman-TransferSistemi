from unicodedata import category

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from transfer.models import Transfer, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Transfer.objects.all()[:4]
    category= Category.objects.all()

    context = {'setting': setting,
               'page':'home',
               'category':category,
               'sliderdata':sliderdata}
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

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir! Teşekkür Ederiz")
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category  = Transfer.objects.all()
    context = {'setting': setting, 'form':form, 'category': category}
    return render(request, 'iletisim.html', context)