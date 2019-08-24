from django.urls import path, include
from .views import *

urlpatterns = [
    path('', studentHomepage, name='studentHomepage'),
    path('apply/', applystudent, name='applystudent'),
]