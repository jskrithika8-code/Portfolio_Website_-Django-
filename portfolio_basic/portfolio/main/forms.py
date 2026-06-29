from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'placeholder': 'Your Name',    'class': 'input'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'Your Email',  'class': 'input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message…', 'class': 'input', 'rows': 5}),
        }
