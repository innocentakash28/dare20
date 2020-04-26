from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start, name='start'),
path('contact', views.contact, name='contact'),
path('privacy', views.privacy, name='privacy'),
path('disclaimer', views.disclaimer, name='disclaimer'),
path('quiz', views.quiz, name='quiz'),
path('tfquiz', views.tfquiz, name='tfquiz'),
path('ynquiz', views.ynquiz, name='ynquiz'),
path('tquiz', views.tquiz, name='tquiz'),
path('ynnquiz', views.ynnquiz, name='ynnquiz')



]