from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView, ListView, DeleteView, CreateView, DetailView, TemplateView, FormView
from .form import Za
from new.models import Customer

def get(request):
    form = Za(request.POST)
    context = {
        'form':Za()
    }
    if request.method == 'POST':
        if form.is_valid():
            print('hello2')
            data = form.cleaned_data
            firstname = data.get('firstname'),
            lastname = data.get('lastname'),
            age = data.get('age')
            comm = data.get('comment')
            print(f'{firstname}{lastname},{age}, {comm}')
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)

class hel(TemplateView):
    template_name = 'hello.html'
    extra_context = {'main': Customer.objects.all().filter(firstname='alex', id = 1)}



def gest(request):
    a = []
    if request.method == 'POST':
        value = request.POST.get('key')
        context = {
            'name':value,
            'a':a
        }
        a.append(value)
    return render(request, 'dz1.html', context)