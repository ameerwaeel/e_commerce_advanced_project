from django import forms

PRODUCT_QUANTITY_CHOICES=[(i,str(i)) for i in range(1,51)]

# class CartAddProductForm(forms.Form):
#     quantity=forms.TypedChoiceField( choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     override=forms.BooleanField(initial=False, required=False,widget=forms.HiddenInput)
    
# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, initial=1)  # Set default quantity to 1
#     override = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int )  # Set default quantity to 1  ,initial=1
    override = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
