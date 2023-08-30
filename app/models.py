from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)



class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50 )
    min_salary =models.BigIntegerField(default =0)
    max_salary = models.BigIntegerField(default=0)
    job_type = models.CharField(max_length=150,default="")
    jobcategory = models.CharField(max_length=150,default="")
    country = models.CharField(max_length=150,default="")
    highestedu = models.CharField(max_length=150,default="")
    experience = models.CharField(max_length=150,default="")
    website = models.CharField(max_length=150,default="")
    shift = models.CharField(max_length=150,default="")
    jobdescription = models.CharField(max_length=500,default="")
    profile_pic = models.ImageField(upload_to="app/img/candidate")



class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo_pic = models.ImageField(upload_to="app/img/company")
