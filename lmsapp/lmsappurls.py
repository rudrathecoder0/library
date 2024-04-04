from django.urls import path 
from . import views

urlpatterns=[
    # path('',views.reload,name='reload'),


    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('registration/',views.registration,name='registration'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
]
