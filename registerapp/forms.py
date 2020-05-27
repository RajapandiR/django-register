from django import forms

from registerapp import models

class RegisterPageForm(forms.ModelForm):
    class Meta:
        model = models.RegisterPage
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'password': forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': 'password'
            }),
            #  'password1': forms.PasswordInput(attrs = {
            #     'class': 'form-control',
            #     'placeholder': 'password1'
            # }),
        }