from django.urls import path
from . import views
urlpatterns = [
    path('',views.studentsignup,name='studentsignup'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('quizhome',views.quizhome,name='quizhome'),
    path('studentlogout',views.studentlogout,name='studentlogout'),
    path('result',views.result,name='result'),
    path('cate/<slug:slug>',views.cate,name='cate')
]
