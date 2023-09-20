from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<h1>Добро пожаловать на главную страницу!</h1><br>'
                        '<a href="/about">О нас</a>')

def about_page(request):
    return HttpResponse('<h1>Какой-нибудь текст</h1><br>'
                        '<a href="/">На главную</a>')

