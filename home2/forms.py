from django import forms
#from django.contrib.auth.models import home2
#from home2.models import Users
from django.contrib.auth.forms import UserRegisterForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Users
        fiels = ['username','email','password1','password2']