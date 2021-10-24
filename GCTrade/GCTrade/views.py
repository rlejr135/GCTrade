import json

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.contrib.auth.hashers import make_password

class MainView(View):
    def get(self, request):
        return render(request, 'GCTrade/Main.html')
