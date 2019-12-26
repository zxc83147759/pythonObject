from django.urls import path
from . import views

app_name = 'encode'
urlpatterns = [
    path('', views.input, name='input'),
    path('result/',views.result,name='result'),
]
