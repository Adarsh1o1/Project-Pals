from django.db import models
from django import forms
from django.forms import ModelForm,widgets
from .models import post
from django.contrib.auth.models import User
from django.contrib import messages



class upload(ModelForm):
    class Meta:
        model=post
        # fields="__all__"
        exclude=["user"]
        # fields=[
        #     "branch",
        #     "year",
        #     "category",
        #     "project_name",
        #     "description",
        #     "image",
        # ]



