from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('blog',views.blog,name='blog'),
    path('images',views.images,name='images'),
    path('registration',views.registration,name='registration'),
    path('logout',views.logout,name='logout'),
    path('post/<str:pk>',views.post,name='post')
]