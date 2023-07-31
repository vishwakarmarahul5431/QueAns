from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Post
from .forms import CreateUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def Home(resquest):
    return HttpResponse("Hellow World")

# @login_required(login_url='login')
def Home_Page(request):

    post=Post.objects.all()
    # answer=Post.objects.all()
    return render(request,'HomePage.html',{'post':post})


def login_view(request):
    if request.user is authenticate:
        return redirect('homepage')
    else:
        if request.user is authenticate:
            return redirect('homepage')
        else:
            if request.method=="POST":
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('homepage')
                else:
                    messages.warning(request,'User Name or Password is Wrong')
                    return render(request,'login.html')
            else:
                return render(request,'login.html')

def Register_view(request):

    if request.user is authenticate:
        return redirect('homepage')
    else:
        if request.method=="POST":
            forms=CreateUserForm(request.POST)
            if forms.is_valid():
                forms.save()
                messages.success(request,'Login Successfull..')
                return redirect('login')
            else:
                messages.warning(request,'Something Went Wrong..')
                return redirect('register')
        else:
            form=CreateUserForm()
            return render(request,'register.html',{'form':form})


def logout_view(request):
    logout(request)
    messages.success(request,'Logout Successfully..')
    return redirect('login')