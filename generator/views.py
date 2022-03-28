from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    thepass = ''
    char_list = list('abcdefghigklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char_list.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        char_list.extend('0123456789')
    if request.GET.get('special'):
        char_list.extend('!@#$%^&*()')

    pass_lenght = int(request.GET.get('len', 12))
    for i in range(pass_lenght):
        thepass += random.choice(char_list)

    return render(request, 'generator/password.html', {'password': thepass})

def about(request):
    return render(request, 'generator/about.html')
