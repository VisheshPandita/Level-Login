from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import studentProfile

# Create your views here.
def studentHomepage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    check = get_object_or_404(studentProfile,user=request.user)
    if check==None:
        return redirect('homepage')    
    return render(request, 'studentHomepage.html', {})

def applystudent(request):
    apply = studentProfile(
        user = request.user
    )
    apply.save()
    return redirect('studentHomepage')    