from django.urls import path, include
from .views import *

urlpatterns = [
    path('', parentHomepage, name='parentHomepage'),
    path('apply/', applyparent, name='applyparent'),
]