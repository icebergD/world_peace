from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def hello(request):
    return HttpResponse("Hello from AvocadOS")

class home(View):
    def get(self, request):
        # if request.user.isauthenticated:
        return render(request, 'base.html', {'a':'b'})