
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from transfer.models import CommentForm, Comment


def index(request):
    return HttpResponse("Transefer Page")

@login_required(login_url='/login')

def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.transfer_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "yorumunuz gönderilmiştir, teşekkürler")

            return HttpResponseRedirect(url)

    messages.warning(request, "yorumunuz kaydedilmedi, lütfen kontrol ediniz")
    return HttpResponseRedirect(url)