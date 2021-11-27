from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 
            'last_name', 
            'email', 
            'address1', 
            'address2', 
            'city', 
            'state', 
            'zip_code', 
            'profile_picture'
        ]