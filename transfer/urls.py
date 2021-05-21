from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment')
     #path('<int:question_id>/', views.detail, name='detail'),
]