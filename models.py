from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_nurse=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)

class Hospital(models.Model):
    Name=models.CharField(max_length=200)
    Phone=models.CharField(max_length=12)
    Place=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Image=models.FileField(upload_to='uploads/')


    def __str__(self):
        return self.Name #doubt

class Nurse(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='nurse') #doubt this line
    Name=models.CharField(max_length=200)
    Phone=models.CharField(max_length=12)
    Email=models.CharField(max_length=200)
    hospital_Name=models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='hospital')

class user(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='user')
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Complaints(models.Model):
    Date=models.DateField()
    Subjects=models.CharField(max_length=200)
    Complaints=models.CharField(max_length=2000)
    User=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='complaints')
    reply=models.TextField(null=True, blank=True)

class Vaccine(models.Model):
    Date=models.DateField()
    Vaccine_name=models.CharField(max_length=200)
    Description=models.CharField(max_length=1000)

    def __str__(self):
        return self.Vaccine_name

class Schedule(models.Model):
    Date = models.DateField()
    Hospital_n = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='hospital_n')
    Vaccine = models.ForeignKey(Vaccine,on_delete=models.CASCADE,related_name='Vaccine')
    Status = models.IntegerField(default=0)
    Start_time = models.TimeField()
    End_time = models.TimeField()

class Appoinment(models.Model):
    User = models.ForeignKey(user,on_delete=models.CASCADE,related_name='complaint')
    Schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE,related_name='complain')
    Status = models.IntegerField(default=0)









