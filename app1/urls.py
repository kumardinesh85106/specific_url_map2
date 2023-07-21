from django.urls import path
from app1.views import *
urlpatterns = [
    path('third/',third,name='third'),
    path('fourth/',fourth,name='fourth'),
]