from django.contrib import messages
from django.shortcuts import render, redirect

from app.filters import userFilter
from app.forms import HospitalForm, NurseForm, UserForm, VaccineForm
from app.models import Hospital, Nurse, user, Complaints, Vaccine, Schedule, Appoinment


def adminpage(request):
    return render(request,'admin_temp/dashboard.html')

def hospital_add(request):                    #http request
    data=HospitalForm()                       #A new instance of HospitalForm with no data, used to display an empty form.
    if request.method=='POST':                #Checks if the request method is POST, indicating that form data has been submitted.
        form=HospitalForm(request.POST,request.FILES)    # A new instance of HospitalForm populated with the submitted data
        if form.is_valid():                            #Checks if the form data is valid according to the form's validation rules.
            form.save()                                #Saves the form data to create a new hospital record in the database.
            return redirect('h_view')                  #Redirects the user to the URL pattern named h_view after successfully saving the form data.
    return render(request,'admin_temp/form.html',{'form':data})   #doubt

def formview(request):      #hospital view     The function name & The HTTP request object.
    print('hy')
    data=Hospital.objects.all()     # A QuerySet containing all records from the Hospital model in the database.
    return render(request,'admin_temp/formview.html',{'form':data})   #doubt form:data

def formedit(request,id):      #hospital edit
    data=Hospital.objects.get(id=id)
    print('esdit')
    if request.method == 'POST':
        print('done')
        form=HospitalForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('h_view')
    else:
        form=HospitalForm(instance=data)

    return render(request,"admin_temp/formedit.html",{'form':form})

def form_del(request,id):         #hospital del
    data = Hospital.objects.get(id=id)
    data.delete()
    return redirect('h_view')


def nurseview(request):
    data=Nurse.objects.all()
    return render(request,'admin_temp/nurse_view.html',{'form':data})

def nurseedit(request,id):
    data=Nurse.objects.get(id=id)
    if request.method == 'POST':
        form=NurseForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('nnurseview')
    else:
        form=NurseForm(instance=data)

    return render(request,"admin_temp/nurse_edit.html",{'form':form})

def nursedel(request,id):
    data = Nurse.objects.get(id=id)
    data.delete()
    return redirect('nnurseview')

def userview(request):                 #added search
    data=user.objects.all()
    UserFilter = userFilter(request.GET,queryset=data)  # UserFilter=variable userFilter= field
    data = UserFilter.qs
    context = {
        'user':data,
        'userfilter':UserFilter,
    }
    return render(request,'admin_temp/user_view.html',context)

def useredit(request,id):
    data=user.objects.get(id=id)
    if request.method == 'POST':
        form=UserForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('uuserview')
    else:
        form=UserForm(instance=data)

    return render(request,'admin_temp/user_edit.html',{'form':data})

def userdel(request,id):
    data = user.objects.get(id=id)
    data.delete()
    return redirect('uuserview')

def admincomplaintview(request):
    data=Complaints.objects.all()
    return render(request,'admin_temp/admin_complaints_view.html',{'form':data})

def comp_reply(request,id):
    data = Complaints.objects.get(id=id)
    return render(request, 'admin_temp/admin_replay.html', {'form': data})

def reply_complaint(request,id):
    complaint = Complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply=r
        complaint.save()
        messages.info(request,'reply send for complaints')
        return redirect('admin_comp_view')
    return render(request,'admin_temp/admin_replay.html',{'form':complaint})

def vaccine_add(request):
    data = VaccineForm()
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('Vaccine')

    return render(request,'admin_temp/vaccine_add.html',{'form':data})
def vaccine_view(request):
    data = Vaccine.objects.all()
    return render(request, 'admin_temp/vaccine_view.html', {'form': data})

def vaccine_edit(request,id):
        data = Vaccine.objects.get(id=id)
        if request.method == 'POST':
            form = VaccineForm(request.POST, request.FILES, instance=data)
            if form.is_valid():
                form.save()
                return redirect('Vaccine_view')
        else:
            form = VaccineForm(instance=data)

        return render(request, 'admin_temp/vaccine_edit.html', {'form': form})
def vaccine_del(request,id):
    data = Vaccine.objects.get(id=id)
    data.delete()
    return redirect('Vaccine_view')
def admin_scheduleview(request):
     data=Schedule.objects.all()   #both user and nurse data view
     return render(request,'admin_temp/adm_schedule_view.html',{'data':data})

def schedule_approve(request,id):
    n=Schedule.objects.get(id=id)
    n.Status=1
    n.save()
    return redirect('admin_sched_view')

def schedule_reject(request,id):
    n=Schedule.objects.get(id=id)
    n.Status=2
    n.save()
    return redirect('admin_sched_view')

def schedule_pending(request,id):
    n=Schedule.objects.get(id=id)
    n.Status=3
    n.save()
    return redirect('admin_sched_view')


def admin_appoinmentview(request):
    data = Appoinment.objects.all()

    return render(request,'admin_temp/admin_appoinment_view.html',{'form':data})

def appoinment_approve(request,id):
    n=Appoinment.objects.get(id=id)
    n.Status=1
    n.save()
    return redirect('admin_appoinment_view')

def appoinment_reject(request,id):
    n=Appoinment.objects.get(id=id)
    n.Status=2
    n.save()
    return redirect('admin_appoinment_view')



