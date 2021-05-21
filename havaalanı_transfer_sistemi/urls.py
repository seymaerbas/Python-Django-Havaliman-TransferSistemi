"""havaalanı_transfer_sistemi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('hakkımızda', views.hakkımızda, name='hakkımızda'),
    path('referanslarımız', views.referanslarımız, name='referanslarımız'),
    path('iletisim', views.iletisim, name='iletisim'),
    path('home/', include('home.urls')),
    path('transfer/', include('transfer.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_transfers, name='category_transfers'),
    path('transfer/<int:id>/<slug:slug>/', views.transfer_detail, name='transfer_detail'),
    path('search/', views.transfer_search, name='transfer_search'),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)