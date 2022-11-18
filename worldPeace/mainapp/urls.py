from django.urls import path
from . import views

urlpatterns = [
    path("", views.home.as_view(), name='home'),
    path("hello", views.hello),

    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]