from django.contrib.auth import forms
from django import forms as form_princ
from django.contrib.auth import get_user_model

class LoginUser(form_princ.Form):
    username =form_princ.CharField(max_length=63,label="Nom d'utilisateur")
    password=form_princ.CharField(max_length=63,widget=form_princ.PasswordInput,label="Mot de passe")

class UserCreationSign(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model=get_user_model()
        fields=['username','email','first_name','last_name']
    

class UserChangeSign(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model=get_user_model()
        fields=['username','email','first_name','last_name','profile_photo',]