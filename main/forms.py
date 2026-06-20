from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField()
    message = forms.CharField()
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Contact
        fields = ("name",)
    
