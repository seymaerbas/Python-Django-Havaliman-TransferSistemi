import json
from unicodedata import category


from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile, FAQ
from reservation.models import Reservation
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



def transfer_search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                transfer = Transfer.objects.filter(title__icontains=query)
            else:

                transfer = Transfer.objects.filter(title__icontains=query, category_id=catid)

            context = {'transfer': transfer,
                       'category': category,
                       }
            return render(request, 'transfer_search.html', context)
    return HttpResponseRedirect('/')

def transfer_search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    transfer = Transfer.objects.filter(title__icontains=q)
    results = []
    for rs in transfer:
      transfer_json = {}
      transfer_json = rs.title
      results.append(transfer_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login hatası ! Lütfen bilgilerinizi kontrol ediniz")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category, }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, "Hoş geldiniz " + current_user.first_name)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category,
               'form': form,
               'setting': setting,
               }

    return render(request, 'signup.html', context)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.filter(status='True').order_by('ordernumber')
    setting = Setting.objects.get(pk=1)
    context = {'faq': faq, 'category': category, 'setting': setting}
    return render(request, 'faq.html', context)

