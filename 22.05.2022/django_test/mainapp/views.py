from django.contrib.auth import logout, authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from mainapp.models import Post
from mainapp.forms import ArtForm
User = get_user_model()


class MainPageView(TemplateView):
    template_name = 'main_page.html'
    extra_context = {'page': Post.objects.all()}



class Login(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'
 

    def post(self, request):
        user = authenticate(
            username=User.objects.get(email=request.POST.get('email')).username,
            password=request.POST.get('password')
        )
        print(user)
        print(request.POST)
        if user:
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {"error": "Что-то не так"})


def logout_func(request):
    logout(request)
    return redirect('/login')


class RegistrationView(LoginRequiredMixin, TemplateView):
    template_name = 'registration.html'


    def post(self, request):
        data = dict(request.POST)
        if data.get('password') == data.get('re_password'):
            user = User.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
            )
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration.html', {'re_password': "Не совпадают"})


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def post(self, request):
        user = request.user
        # users = user.__class__.objects.filter(pk=user.pk)
        # users.update(**request.POST)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('/')

class Posts(View):
    template_name = 'main_page.html'
    model = Post
    form_class = FormView
    
    def form_valid(self, form):
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = self.request.user
            form.save()   
            return redirect('/')

    
