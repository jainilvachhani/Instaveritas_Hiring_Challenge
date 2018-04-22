# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Book,Theatre
from django.shortcuts import render

# Create your views here.

def post_list(request):
    theatre =  Theatre.objects.all()
    return render(request, 'book_tickets/post_list.html', {'theatre':theatre})
    
def add(request):
    print("DDSS")
    #query = Book.objects.filter(theatre_name = t,)