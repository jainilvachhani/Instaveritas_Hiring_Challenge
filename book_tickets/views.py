# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Book,Theatre
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import urllib
# Create your views here.


def post_list(request, flag=False):
    theatre =  Theatre.objects.all()
    #flag = False
    return render(request, 'book_tickets/post_list.html', {'theatre':theatre, 'flag': flag})
    
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
        else:
            Book.objects.create(theatre_name = theatre, timeslot = time, date = d)
        return redirect('post_list')