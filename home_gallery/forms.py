from django import forms
from contact_us.models import ContactForm


class ContactFormClass(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name', 'name':'name', 'id':'name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Your Email', 'name':'email', 'id':'email'}),
        'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject', 'name':'Subject', 'id':'Subject'}),
        'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Message', 'name':'Message', 'id':'Message' , 'cols':'30', 'rows':'10'}),
        }
