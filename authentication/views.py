from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

# LOGIN VIEW ENDPOINT

def loginuser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully Logged in')
            return redirect('posts')
        else:
            messages.error(request, 'Invalid Username or password')
    return render(request, 'login.html')

from .forms import SignUpForm
def register(request):
    if request.method=="POST":

        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignUpForm()   
    return render(request, 'register.html',{'form':form})
