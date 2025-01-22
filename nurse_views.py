from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import NurseForm, LoginForm, ComplaintsForm, ScheduleForm
from app.models import Nurse, Complaints, Schedule


def nurse_dash(request):
    return render(request,'nurse_temp/nursedash.html')


def nursecomplaints(request):
    user=request.user           #doubt
    data=ComplaintsForm()
    if request.method =='POST':
        form=ComplaintsForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False) #form
            obj.User=user
            obj.save()
            messages.info(request,'Complaints successfully registered')
            return redirect('nursecomplaints_view')
    return render(request,'nurse_temp/nurse_complaints_add.html',{'form':data})

def nursecomplaintsview(request):
    data=Complaints.objects.filter(User=request.user)
    return render(request,'nurse_temp/nurse_complaint_view.html',{'form':data})

def nursecomplaintsedit(request,id):
    data=Complaints.objects.get(id=id)
    if request.method == 'POST':
        form=ComplaintsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('nursecomplaints_view')
    else:
        form=ComplaintsForm(instance=data)

    return render(request,'nurse_temp/nurse_complaints_edit.html',{'form':form})

def nursecomplaintsdel(request,id):
    data =Complaints.objects.get(id=id)
    data.delete()
    return redirect('nursecomplaints_view')

def scheduleadd(request):
    form=ScheduleForm()
    n= request.user
    d=Nurse.objects.filter(user=n).first()
    u=d.hospital_Name       #doubt
    if request.method == 'POST':
        form=ScheduleForm(request.POST)
        if form.is_valid():
            obj =form.save(commit=False)
            obj.Hospital_n=u
            obj.save()
            messages.info(request,'Vaccination schedule added Successfully')
            return redirect('schedule_view')

    return render (request,'nurse_temp/schedule_add.html',{'form':form})

def scheduleview(request):
    data=Schedule.objects.all()
    return render(request,'nurse_temp/schedule_view.html',{'form':data})



def scheduleedit(request,id):
    data=Schedule.objects.get(id=id)
    if request.method == 'POST':
        form=ScheduleForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('schedule_view')
    else:
        form=ScheduleForm(instance=data)

    return render(request,'nurse_temp/schedule_edit.html',{'form':form})


def scheduledel(request,id):
    data =Schedule.objects.get(id=id)
    data.delete()
    return redirect('schedule_view')

