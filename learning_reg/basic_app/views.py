from django.shortcuts import render
from .forms import UI,UI2
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'basic_app/homepage.html')


@login_required
def user_special(request):
    return HttpResponse('you are logged in nice!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered=False
    if request.method == "POST":
        user_form=UI(data=request.POST)
        profile_form=UI2(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print('error')
    else:
        user_form=UI()
        profile_form=UI2()
    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')
        else:
            return HttpResponse("the user is not a active user")
    else:
        return render(request,'basic_app/login.html',{})


