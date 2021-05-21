from unicodedata import category

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from transfer.models import Transfer, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Transfer.objects.all()[:4]
    category= Category.objects.all()
    daytransfer=Transfer.objects.all()[:4]
    lasttransfer=Transfer.objects.all().order_by('-id')[:4]
    randomtransfer = Transfer.objects.all().order_by('?')[:4]
    context = {'setting': setting,
               'page':'home',
               'category':category,
               'sliderdata': sliderdata,
               'daytransfer':daytransfer,
               'lasttransfer': lasttransfer,
               'randomtransfer': randomtransfer
               }
    return render(request, 'index.html', context)

def hakkımızda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'hakkımızda', 'category': category}
    return render(request, 'hakkımızda.html', context)

def referanslarımız(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'referanslarımız', 'category': category}
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
    category = Category.objects.all()
    context = {'setting': setting, 'form':form, 'category': category}
    return render(request, 'iletisim.html', context)




def category_transfers(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    transfers =Transfer.objects.filter(category_id=id,  status='True')
    context = { 'category': category,
                'transfers': transfers,
                'categorydata':categorydata,
                }
    return render(request, 'transfers.html', context)

def transfer_detail(request, id, slug):
    category = Category.objects.all()
    transfer = Transfer.objects.get(pk=id)
    comments = Comment.objects.filter(transfer_id=id, status='True')
    images = Images.objects.filter(transfer_id=id)
    context = {'category': category,
               'transfer': transfer,
               'images':images,
               'comments': comments
               }
    return render(request, 'transfer_detail.html',context)