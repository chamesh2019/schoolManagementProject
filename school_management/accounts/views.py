from django.shortcuts import render
from django.contrib.auth import authenticate


def login(request):
    return render(request, 'accounts/base.html', {})


def register(request):
    return render(request, 'accounts/base.html', {})
