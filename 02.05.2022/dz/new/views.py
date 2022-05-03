
from django.http import HttpResponse
from django.shortcuts import render,  redirect
from django.views import View
import requests
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from new.models import AnimalImage, Species


class Po(View):
    def get(self, request):
        return render(request, "sel.html")
    
    def post(self, request):
        if request.POST.get('cats'):
            data = requests.get('https://aws.random.cat/meow').json()
            context = {
                'main': data['file'],
                'animal': 'cat'
            }
            request.session['context'] = context
            return redirect('animal')
        elif request.POST.get('dogs'):
            data = requests.get('https://dog.ceo/api/breeds/image/random').json()
            context = {
                'main': data['message'],
                'animal': 'dog',
            }
            request.session['context'] = context
            return redirect('animal')
      
class Lo(View):
    def get(self, request):
        if request.session.has_key('context'):
            username = request.session['context']
            return render(request, 'nes.html', username)
        return render(request, 'nes.html')

    def post(self, request):
        username = request.session['context']
        email = request.POST.get('email')
        if request.POST.get('save'):
            if username['animal'] == 'dog':
                AnimalImage.objects.create(url = username['main'], species = Species.objects.get(id = 2), type = 'jpg' )
            elif username['animal'] == 'cat':
                AnimalImage.objects.create(url = username['main'], species = Species.objects.get(id = 1), type = 'jpg' )

            message = render_to_string('email.html', {
                'mess': username['main']
            }) 
            try:
                mail = EmailMessage('вам', message, to=[email])
                mail.send()
            except Exception as e:
                print(e)
            return HttpResponse('Ваше сообщение отправлено на почту')