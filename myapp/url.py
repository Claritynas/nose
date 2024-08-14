from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('blog',views.blog,name='blog'),
    path('insurance',views.insurance,name='insurance'),
    path('registration',views.registration,name='registration')
]