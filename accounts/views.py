from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from .forms import LoginForm, RegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class IndexView(View):
    def get(self, request, *args, **kwargs):
        print("index")
        lang = request.session.get('hoge')
        # name = request.session['hoge']
        print(lang)
        return HttpResponse("You're looking at question %s.")

    def post(self, request, *args, **kwargs):
        print("post")
        return HttpResponse("post")

class HelloView(TemplateView):
    template_name = "accounts/hello.html"

class UserView(TemplateView):
    template_name = "accounts/user.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] =  'toyooka'
        return context
class ListView(TemplateView):
    template_name = "accounts/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        l_empty = ['toyooka', 'toyooka2']
        context["lists"] =  l_empty
        return context

class Top(generic.TemplateView):
    template_name = 'accounts/top.html'

# class Login(View):
#     """ログインページ"""
#     form_class = LoginForm
#     template_name = 'accounts/login.html'


class Logout(LogoutView):
    def get(self, request, *args, **kwargs):
        print("index")
        return HttpResponse("You're looking at question %s.")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        print("d")
        form = LoginForm(request.POST)
        template_name = 'accounts/login.html'
        print("get")
        return render(request, template_name,  { 'form': form })

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        print("form")
        template_name = 'accounts/top.html'
        is_valid = form.is_valid()
        if not is_valid:
            template_name = 'accounts/login.html'
            return render(request, template_name, { 'form': form })
        request.session['hoge'] = 'su!'
        return render(request, template_name)

# def login(request):
#     if request.method == 'GET':
#         print("d")
#         form = LoginForm(request.POST)
#         template_name = 'accounts/login.html'
#         print("get")
#         return render(request, template_name,  { 'form': form })

#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         print("form")
#         template_name = 'accounts/top.html'
#         is_valid = form.is_valid()
#         if not is_valid:
#             print(form)
#             template_name = 'accounts/login.html'
#             return render(request, template_name, { 'form': form })
#         return render(request, template_name, { 'form': form })
index = IndexView.as_view()
hello = HelloView.as_view()
user = UserView.as_view()
list = ListView.as_view()
login = LoginView.as_view()
# def index(request):
#     print("index")
#     return HttpResponse("You're looking at question %s.")

# def get(request, id):
#     print("get")
#     return HttpResponse("GET" + id)
