from django.forms import ModelForm
from .models import *
class rw(ModelForm):
    class Meta:
        model=regis
        fields="__all__"
class k(ModelForm):
    class Meta:
        model=key
        fields=["ke"]
class quest(ModelForm):
    class Meta:
        model=questions
        fields=['question','question1','question2','question3','question4',"answer"]