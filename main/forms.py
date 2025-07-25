from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form with proper styling and validation"""
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'inquiry_type', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name *',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address *',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number (Optional)'
            }),
            'inquiry_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject *',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message *',
                'rows': 6,
                'required': True
            }),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
        return email
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name.strip()) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name.strip() if name else name