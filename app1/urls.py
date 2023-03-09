from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
path('practice/',practice,name='practice'),
path('end/',end,name='end'),
]