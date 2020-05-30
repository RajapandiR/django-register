from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from registerapp import models

class RegisterPageForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password' })) 
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password' }))
    class Meta:
        model = models.RegisterPage
        fields = ('name', 'email', 'password1', 'password2')
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = models.RegisterPage.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email alread exists")
        return email
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = models.RegisterPage
        fields = ('email','password')
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Login")

    