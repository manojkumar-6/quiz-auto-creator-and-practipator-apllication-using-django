from pyexpat import model
from django.db import models

# Create your models here.
class regis(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return"{0.name}{0.email}{0.password}".format(self)
class key(models.Model):
    ke=models.CharField(max_length=6)
    j=models.CharField(max_length=20)
    def __str__(self):
        return "{0.ke}{0.j}".format(self)
class score(models.Model):
    se=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    participated=models.CharField(max_length=10)
    def __str__(self):
        return"{0.se}{0.name}{0.participated}".format(self)

class questions(models.Model):
    question=models.CharField(max_length=20)
    question1=models.CharField(max_length=20)
    question2=models.CharField(max_length=20)
    question3=models.CharField(max_length=20)
    question4=models.CharField(max_length=20)
    answer=models.CharField(max_length=20)
    key=models.CharField(max_length=10)
    def __str__(self):
        return"{0.question}{0.question1}{0.question2}{0.question3}{0.question4}{0.answer}{0.key}".format(self)