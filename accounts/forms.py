from django import forms
from .models import *


class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','country']

    def clean(self):
        cleaned_data=super(RegisterForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('your password don\'t match')    
        return cleaned_data                                 
    
    def __init__(self,*args, **kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='enter first name'
        self.fields['last_name'].widget.attrs['placeholder']='enter last name'
        self.fields['phone_number'].widget.attrs['placeholder']='enter phone number'
        self.fields['email'].widget.attrs['placeholder']='enter email'
        self.fields['password'].widget.attrs['placeholder']='enter password'
        self.fields['confirm_password'].widget.attrs['placeholder']='enter confirm password'

