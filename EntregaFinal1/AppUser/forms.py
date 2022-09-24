from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppUser.models import Avatar




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    telefono = forms.IntegerField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'telefono')
        
        
        
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "__all__"
        