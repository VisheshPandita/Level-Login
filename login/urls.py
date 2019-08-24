from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage, name='loginHomepage'),
    path('register/', register, name='register'),
    path('logout/', logout_request, name='logout'),
    path('login/', login_request, name='login'),  
]