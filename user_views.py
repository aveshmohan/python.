

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render

from app.forms import LoginForm, UserForm, ComplaintsForm, ScheduleForm
from app.models import Complaints, Schedule, Appoinment, user


def user_dash(request):
    return render(request,'user_temp/userdash.html')

def usercomplaints(request):
    user=request.user
    data=ComplaintsForm()
    if request.method =='POST':
        form=ComplaintsForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.User=user
            obj.save()
            messages.info(request,'Complaints successfully registered')
            return redirect('usercomplaint_view')
    return render(request,'user_temp/user_complaints.html',{'form':data})

def usercomplaintsview(request):
    data=Complaints.objects.filter(User=request.user)
    return render(request,'user_temp/user_complaint_view.html',{'form':data})

def usercomplaintsedit(request,id):
    data=Complaints.objects.get(id=id)
    print('hyyy')
    if request.method == 'POST':
        form=ComplaintsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('usercomplaint_view')
    else:
        form=ComplaintsForm(instance=data)

    return render(request,'user_temp/user_complaints_edit.html',{'form':form})

def usercomplaintsdel(request,id):
    data =Complaints.objects.get(id=id)
    data.delete()
    return redirect('usercomplaint_view')#doubt return redirect and render difference

def userschedule_view(request):
    data=Schedule.objects.filter(Status=1)
    return render(request,'user_temp/user_schedule_view.html',{'form':data})




def bookappoinment(request,id):           #doubt
    schedule = Schedule.objects.get(id=id)
    u = user.objects.get(user=request.user)
    appoinment = Appoinment.objects.filter(User=u,Schedule=schedule) #field= value
    if appoinment.exists():
        messages.info(request,'you have alredy booked')
        return redirect('user_schedule_view')
    else:
        if request.method == 'POST':
            obj = Appoinment()
            obj.User = u
            obj.Schedule  = schedule #field = value
            obj.save()
            messages.info(request,'Appoinment booked')
            return redirect('book_appoinment')

    return render(request,'user_temp/book_appoinment_add.html',{'form':schedule})


def userappoinment_view(request):
    u = user.objects.get(user=request.user)
    data= Appoinment.objects.filter(User=u)

    return render(request,'user_temp/appoinment_view.html',{'form':data})
