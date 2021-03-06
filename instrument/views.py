from django.contrib import messages
from django.urls import reverse
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import TickerForm,InstrumentForm,StockForm
from .models import Instrument,Stock
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView

import requests,threading,json
from .api import API


@login_required
def add_view(request):
    form_add=InstrumentForm(request.POST or None)
    form=TickerForm(request.POST or None)
    if request.method=="POST":
        if form_add.is_valid():
            data=InstrumentForm(request.POST)
            obj=data.save(commit=False)
            obj.profiles=request.user
            obj.save()
            return HttpResponseRedirect(reverse("add"))
            
        elif form.is_valid():
            ticker=request.POST['ticker']
            return HttpResponseRedirect(ticker)
        else:
            form=TickerForm()
            form_add=InstrumentForm()

    context={
        "form":form,
        "form_if":form_add,
    }
    return render(request,"instrument/add.html",context)

@login_required
def quote(request):
    form=TickerForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            ticker=request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form=TickerForm()
    context={
        "form":form,
    }
    return render(request,'instrument/quote.html',context)

@login_required
def instrument_list(request):
    user=request.user
    queryset=Instrument.objects.filter(profiles=user).order_by('-total_price')
    context = {
        "qs":queryset
    }
    return render(request,"instrument/list.html",context)

@login_required
def update(request,pk):
    obj=Instrument.objects.get(id=pk)
    form_upd=InstrumentForm(instance=obj)
    form=TickerForm(request.POST or None)
    if request.method=="POST":
        form_upd=InstrumentForm(request.POST,instance=obj)
        if form_upd.is_valid():
            form_upd.save()
            return HttpResponseRedirect(reverse("instrument_list"))
            
        elif form.is_valid():
            ticker=request.POST['ticker']
            return HttpResponseRedirect(ticker)
        else:
            form=TickerForm()
            form_add=InstrumentForm()

    context={
        'object':obj,
        "form_if":form_upd,
        "form":form,

    }
    return render(request,"instrument/update.html",context)

@login_required
def delete(request,pk):
    obj=Instrument.objects.get(id=pk)
    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect(reverse("instrument_list"))

    context={'object':obj}
    return render(request,"instrument/delete.html",context)

@login_required
def research(request):
    import requests
    import json

    if request.method=="POST":
        ticker_cl=request.POST['ticker_cl'].upper()
        api_request=requests.get("https://cloud.iexapis.com/stable/stock/" + ticker_cl + "/quote?token="+ API)
        try:
            api=json.loads(api_request.content)
        except:
            api="Error"
        context={
            "ticker_cl":ticker_cl,
            "api":api
        }
        return render(request,'instrument/research.html',context)
        
    else:
        return render(request,'instrument/research.html',{'ticker':"Enter a Ticker symbol above"})

@login_required
def watchlist(request):
    user=request.user
    form=TickerForm(request.POST or None)
    form_add=StockForm(request.POST or None)
    if request.method=="POST":
        if form_add.is_valid():
            data=StockForm(request.POST)
            obj=data.save(commit=False)
            obj.profiles=request.user
            obj.save()
            messages.success(request,("Stock has been added! "))
            return HttpResponseRedirect(reverse("watchlist"))
        elif form.is_valid():
            ticker=request.POST['ticker']
            return redirect(ticker)
    else:
        stock_qs=Stock.objects.filter(profiles=user)
        tickers=[]
        threads=[]
        output=[]

        for i in stock_qs:
            tickers.append(i)

        def get_data(ticker):
            data=[]
            api_request=requests.get(("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_4d146da815d147cdbdd02ff2f0badcbc"))
            api=json.loads(api_request.content)
            data.append(i.id)
            data.append(api)
            output.append(data)
            return api

        for i in tickers:
            try:
                x=threading.Thread(target=get_data,args=(i.ticker,))
                x.start()
                threads.append(x)
            except Exception as e:
                i.delete()


        for thread in threads:
            thread.join()


    context={
        "form":form,"form_add":form_add,"output":output
        }
    return render(request,'instrument/watchlist.html',context)

def unfollow(request,pk):
    obj=Stock.objects.get(id=pk)
    obj.delete()
    messages.success(request,("Stock has been unfollowed "))
    return HttpResponseRedirect(reverse("watchlist"))
