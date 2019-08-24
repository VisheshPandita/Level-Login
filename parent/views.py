from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import ParentProfile

# Create your views here.
def parentHomepage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    check = get_object_or_404(ParentProfile,user=request.user)
    if check==None:
        return redirect('homepage')     
    return render(request, 'parentHomepage.html', {})

def applyparent(request):
    apply = ParentProfile(
        user = request.user
    )
    apply.save()
    return redirect('parentHomepage')    