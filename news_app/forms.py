from django import forms
from .models import  Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Replace 'Contact' with your actual model name
        fields = '__all__'  # Include all fields from the model
