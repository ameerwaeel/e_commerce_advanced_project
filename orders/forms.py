from django import forms 
from .models import *
from django.core.exceptions import ValidationError



class OrderCreateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','adress','postal_code','city']
 
class OrderPayForm(forms.ModelForm):
    
    class Meta:
        model = OrderPay
        fields = ('pay_image','pay_phone')



       
    def clean_pay_phone(self):
        pay_phone=self.cleaned_data.get('pay_phone')
        if not pay_phone.isdigit():
            raise ValidationError('the phone number must contain only digites')
        if len(pay_phone) != 11 :
            raise ValidationError('the phone number must contain only 11 number')
        valied_prefixes=['010','011','012','015']
        if not any(pay_phone.startswith(prefix) for prefix in valied_prefixes):
            raise ValidationError('the phone number must start with (010 /011 /012 /015)')

        return pay_phone



# class OrderPayForm(forms.ModelForm):
#     class Meta:
#         model = OrderPay
#         fields = ('pay_image', 'pay_phone')

#     def clean_pay_phone(self):
#         pay_phone = self.cleaned_data.get('pay_phone')

#         # Check if the phone number contains only digits
#         if not pay_phone.isdigit():
#             raise ValidationError('The phone number must contain only digits.')

#         # Check if the phone number length is exactly 11
#         if len(pay_phone) != 11:
#             raise ValidationError('The phone number must contain exactly 11 digits.')

#         # Check if the phone number starts with valid prefixes
#         valid_prefixes = ['010', '011', '012', '015']
#         if not any(pay_phone.startswith(prefix) for prefix in valid_prefixes):
#             raise ValidationError('The phone number must start with (010, 011, 012, 015).')

#         return pay_phone