from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import teacherProfile

# Create your views here.
def teacherHomepage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    check = get_object_or_404(teacherProfile,user=request.user)
    if check==None:
        return redirect('homepage')     
    return render(request, 'teacherHomepage.html', {})

def applyteacher(request):
    apply = teacherProfile(
        user = request.user
    )
    apply.save()
    return redirect('teacherHomepage')    