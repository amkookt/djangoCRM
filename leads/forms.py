from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from .models import Lead,User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username':UsernameField}
       
        

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
            # 'description',
            # 'phone_number',
            # 'email',
            # 'profile_picture'
        )
