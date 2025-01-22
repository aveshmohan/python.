from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Login, Hospital, Nurse, user, Complaints, Vaccine, Schedule


class DateInput(forms.DateInput):
    input_type= 'Date'


class TimeInput(forms.TimeInput):
    input_type='time'
class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput,)
    password2=forms.CharField(label='confirm Paswword',widget=forms.PasswordInput,)

    class Meta:
        model=Login #doubt model
        fields=('username','password1','password2')

class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields='__all__'

class NurseForm(forms.ModelForm):
    class Meta:
        model=Nurse
        fields=('Name','Phone','Email','hospital_Name')

class UserForm(forms.ModelForm):
    class Meta:
        model=user
        fields=('Name','Place','Phone')

class ComplaintsForm(forms.ModelForm):
    Date=forms.DateField(widget=DateInput)
    class Meta:
        model=Complaints
        fields=('Date','Subjects','Complaints')

class VaccineForm(forms.ModelForm):
    Date=forms.DateField(widget=DateInput)
    class Meta:
        model=Vaccine
        fields='__all__'

class ScheduleForm(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)
    Start_time = forms.TimeField(widget=TimeInput)
    End_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Schedule
        fields = ('Date','Vaccine','Start_time','End_time')



