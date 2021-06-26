from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendreserve/<int:id>', views.sendreserve, name='sendreserve'),
     #path('<int:question_id>/', views.detail, name='detail'),
]