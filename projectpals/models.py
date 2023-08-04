from django.db import models
from django.contrib.auth.models import User
from django import forms

class category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name




class post(models.Model):
    # current_user=.user
    # users=us.username
    # name=models.CharField(max_length=20,default="")
    # user=models.username()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch=models.CharField(max_length=20,default="")
    FRESHMAN = '1st'
    SOPHOMORE = '2nd'
    JUNIOR = '3rd'
    SENIOR = '4th'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, '1st'),
        (SOPHOMORE, '2nd'),
        (JUNIOR, '3rd'),
        (SENIOR, '4th'),
    ]
    year= models.CharField(
        max_length=3,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    category=models.ForeignKey(category,default=True,on_delete=models.CASCADE,null=False)
    project_name=models.CharField(max_length=20,default="")
    description= models.TextField()
    image=models.ImageField(upload_to='projectpals/images',default="")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.project_name

