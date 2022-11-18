from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
def hello(request):
    return HttpResponse("Hello from AvocadOS")

class home(View):
    def get(self, request):
        # if request.user.isauthenticated:
        return render(request, 'base.html', {'a':'b'})

class studentList(View):
    def get(self, request):
        if request.user.isauthenticated:
            students = list(MUser.objects.all().values())#.order_by('-created')
            return render(request, 'studentList.html', {'students':students})
        else:
            return redirect('login')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('home')
        else:
            return reverse_lazy('client-home')


def logout_user(request):
    logout(request)
    return redirect('login')