# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Book,Theatre
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import urllib
# Create your views here.


def post_list(request, flag=False, query = False):
    theatre =  Theatre.objects.all()
    #flag = False
    return render(request, 'book_tickets/post_list.html', {'theatre':theatre, 'flag': flag, 'query': query,})
    
def post(request,flag,query):
    theatre =  Theatre.objects.all()
    #flag = False
    return render(request, 'book_tickets/post.html', {'theatre':theatre, 'flag': flag, 'query': query,})
    
    
def add(request):
    if request.method == 'POST':
        theatre = request.POST.get('theatre')  
        day = request.POST.get('day')
        month = request.POST.get('month')
        time = int (request.POST.get('time'))
        d = '2018-' + month + '-' + day + ' 00:00:00'
        query = Book.objects.filter(theatre_name = theatre, timeslot = time, date = d)
        print("query")
        if (query.exists()):
            #kwargs['flag'] = True
            flag = True
            print("No cant's do")
            return post(request, True, False)
            
        else:
            Book.objects.create(theatre_name = theatre, timeslot = time, date = d)
        return post(request, False, False)
        
def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        query = Theatre.objects.filter(theatre_name = query)
        if(query.exists()):
            return post(request, False, True)
        else:
            return post(request, False, True)
        