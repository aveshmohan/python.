from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from app.forms import HospitalForm, LoginForm, NurseForm, UserForm
from app.models import  Hospital


# Create your views here.
def demo(request):
    return render(request,'index.html')


def user(request):           #user reg
    user_form = LoginForm()
    customer_form = UserForm()
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        customer_form = UserForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user=user_form.save(commit= False)
            user.is_user= True
            user.save()
            user1 = customer_form.save(commit=False)
            user1.user = user #doubt which user
            user1.save()
            messages.info(request, 'User Registered Sucessfully')
            return redirect('uuser')
    return render(request, 'userregform.html', {'user_form': user_form,'customer_form':customer_form})


def Nurse_reg(request):
    user_form=LoginForm()
    nurse_form=NurseForm()
    if request.method =='POST':
        user_form=LoginForm(request.POST)
        nurse_form=NurseForm(request.POST)
        if user_form.is_valid() and nurse_form.is_valid():
            user=user_form.save(commit= False)
            user.is_nurse= True
            user.save()

            nurse=nurse_form.save(commit =False)
            nurse.user=user
            nurse.save()
            messages.info(request, 'Nurse Registered Sucessfully')
            return redirect('nurse_reg')
    return render(request,'nurse_reg.html',{'user_form':user_form,'nurse_form':nurse_form})



def login_view(request):
    print("hi")
    if request.method =='POST':
        print("hello")
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        print(username,password)
        user=authenticate(request,username=username,password=password) #authenticate check chayan ulla oru function anu red username modelil koduthathanu white variable
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin')
            elif user.is_nurse:
                return redirect('nursedashboard')
            elif user.is_user:
                return redirect('userdashboard')

        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'loginpage.html')

def log_out(request):
    logout(request)
    return redirect('demo')




