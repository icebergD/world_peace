from django.urls import path
from . import views

urlpatterns = [
    path("", views.home.as_view(), name='home'),
    path("hello", views.hello),
    path('student-list', views.studentList.as_view(), name='student-list'),
    path('respond-on-user', views.respondOnUser.as_view(), name='respond-on-user'),
    path('vacancy-list', views.vacancyList.as_view(), name='vacancy-list'),
    path('respond-on-vacancy', views.respondOnVacancy.as_view(), name='respond-on-vacancy'),

    path('user-accaunt', views.userAccaunt.as_view(), name='user-accaunt'),
    path('busines-accaunt', views.businesAccaunt.as_view(), name='busines-accaunt'),

    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]