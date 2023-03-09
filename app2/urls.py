from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('smart_work/',smart_work,name='smart_work'),
    path('friend/',friend,name='friend'),
]