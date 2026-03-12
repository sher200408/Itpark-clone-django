from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomProfileCreationForm, CustomUserCreationForm
from django.contrib import messages

from .models import Profil
# Create your views here.

def profiles_skill(request):
    users = Profil.objects.all()
    context = {
        "users_one":users
    }
    return render(request,"users/users.html",context)

def profile(request,id):
    profile = Profil.objects.get(id=id)
    context = {
        "profile":profile 
    }
    return render(request,"users/profile.html",context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request ,"Welcome")
            return redirect("profiles")
        else:
            messages.error( request ,"XAto berdi")
        
    return render(request,"users/login.html")


def logouts(request):
    logout(request)
    messages.info( request,"Exite")
    return redirect('login')

def register_user_signup(request):
    form =  CustomUserCreationForm()
    for  f  in  form:
        if f.label == "Password":
            f.label = "Parol"
        elif f.label == "Password confirmation":
            f.label = "Parol Tekshirish"
            
    context = {
        'form':form
    }
    if request.method == "POST":
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request,user)
            
            messages.success( request,"Foydalanuchi Ro'yihatdan otdi")
            return redirect('profiles')
        else:
            messages.error(request,"foydalanychi o'tmadim ")
        
    return render(request, 'users/register.html',context) 

@login_required(login_url='login')
def account_user(request):
    # profil = request.user.profil
    profil = Profil.objects.filter(user=request.user).first()
    context = {
        'profil':profil
    }
    return render(request,'users/account_user.html',context)

@login_required(login_url='login')
def account_edit(request):
    # profil = request.user.profil
    profil = Profil.objects.filter(user=request.user).first()
    form  = CustomProfileCreationForm(instance=profil)
    if request.method == "POST":
        form = CustomProfileCreationForm(request.POST,request.FILES,instance=profil)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
        "form":form
    }
    
    return render(request,'users/account_edit.html',context)
