
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from main.froms import Mian

class Mains(View):
    def get(self, request):
        form = Mian
        context = {
            'main': form
        }
        return render(request, 'mian.html', context)

    def post(self, request):
        print('hello')
        if request.method == 'POST':
            form = Mian(request.POST)
            print('hello1')
            if form.is_valid():
                print('hello2')
                data = form.cleaned_data
                firstname = data.get('firstname'),
                lastname = data.get('lastname'),
                age = data.get('age')
                print(f'{firstname}{lastname},{age}')
                return render(request, 'otvet.html', data)



class Lol(View):
    def get(self, request):
        return render(request, 'mian.html')
