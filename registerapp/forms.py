from django import forms
from passlib.hash import pbkdf2_sha256

from registerapp import models

class RegisterPageForm(forms.ModelForm):
    # password = forms.CharField(max_length=8)
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password' }))
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
             'confirmPassword': forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': 'confirm password'
            }),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = models.RegisterPage.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    
    def verify_paaword(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)

    def clean_confirmPassword(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirmPassword")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2