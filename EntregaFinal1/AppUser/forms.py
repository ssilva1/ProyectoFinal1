from django import forms
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth.models import User

from AppUser.models import Avatar




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    telefono = forms.IntegerField(required=False)
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'email', 'telefono','password1', 'password2')
        
        
        
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"
        
        
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    telefono = forms.IntegerField(required=False)
    # password = forms.CharField()
    # password2 = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'telefono',]
        help_texts = {k: "" for k in fields}
        
