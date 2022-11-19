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
        # if request.user.is_authenticated:
        # return render(request, 'base.html', {'a':'b'})
        return redirect('login')
class studentList(View):
    def get(self, request):
        if request.user.is_authenticated:
            students = list(MUser.objects.all().values())#.order_by('-created')
            students_list = []
            print(students)
            for i in students:
                category = Category.objects.filter(id=i['category_id']).values('title')
                el = {'student': i, 'category': category[0]['title']}
                students_list.append(el)

            return render(request, 'studentList.html', {'students': students_list})
        else:
            return redirect('login')
class respondOnUser(View):
    def post(self, request):
        if request.user.is_authenticated:
            muser_id = request.POST.get('muser_id')
            ur = RespondersForBusines(
                s_user=MUser.objects.get(id=muser_id),
                b_user=Busines.objects.get(user=request.user)
            )
            ur.save()
            return redirect('student-list')
        else:
            return redirect('login')

class vacancyList(View):
    def get(self, request):
        if request.user.is_authenticated:
            vacancy = list(Vacancy.objects.all().values())#.order_by('-created')

            vacancy_list = []
            for i in vacancy:
                category = Category.objects.filter(id=i['category_id']).values('title')
                el = {'vacancy': i, 'category': category[0]['title']}
                vacancy_list.append(el)

            return render(request, 'vacancyList.html', {'vacancy': vacancy_list})
        else:
            return redirect('login')
class respondOnVacancy(View):
    def post(self, request):
        if request.user.is_authenticated:
            vacancy_id = request.POST.get('vacancy_id')

            ur = RespondersForUser(
                s_user=MUser.objects.get(user__id=request.user.id),
                vacancy=Vacancy.objects.get(id=vacancy_id)
            )
            ur.save()
            return redirect('vacancy-list')
        else:
            return redirect('login')

class userAccaunt(View):
    def get(self, request):
        if request.user.is_authenticated:
            resume = MUser.objects.filter(user__id=request.user.id).values().first()
            responders = RespondersForBusines.objects.filter(s_user__user__id=request.user.id).values()
            responders_list = []
            for i in responders:
                busines = list(Busines.objects.filter(id=i['b_user_id']).values())
                responders_list.append(busines)

            achive = Achive

            category = Category.objects.filter(id=resume['category_id']).values().first()['title']
            return render(request, 'userAccaunt.html', {'resume': resume, 'responders': responders_list, 'achive': achive, 'category': category})
        else:
            return redirect('login')

class businesAccaunt(View):
    def get(self, request):
        if request.user.is_authenticated:
            busines = Busines.objects.filter(user=request.user).values().first()
            responders = RespondersForUser.objects.filter(vacancy__busines__id=busines['id']).values()
            responders_list = []
            for i in responders:
                vacancy = Vacancy.objects.filter(id=i['vacancy_id']).values().first()
                user = MUser.objects.filter(id=i['s_user_id']).values().first()
                el = {
                    'vacancy':vacancy,
                    'user':user
                }
                responders_list.append(el)
            return render(request, 'businesAccaunt.html', {'busines': busines, 'responders': responders_list})
        else:
            return redirect('login')

class tutorials(View):
    def get(self, request):
        if request.user.is_authenticated:

            return render(request, 'tutorials.html')
        else:
            return redirect('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        print()
        if len(list(Busines.objects.filter(user=self.request.user.id))) >0:
            return reverse_lazy('student-list')
        elif len(list(MUser.objects.filter(user=self.request.user.id))) > 0:
            return reverse_lazy('tutorials')
        else:
            return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')