from django.urls import path  # url 경로 import
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),  # members url 제작후 여기에 view에 쓴 내용을 담아온다
    path('syntax/', views.syntax, name='syntax'),
    path('ifelse/', views.ifelse, name='ifelse'),
    path('forloop/', views.forloop, name='forloop'),
]
