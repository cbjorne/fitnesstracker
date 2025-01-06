from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'login__input',
            'placeholder': 'Enter Username',
            'type': 'text' }), 
        label='username', 
        max_length=20)
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'login__input',
            'placeholder': 'Enter Password',
            'type': 'password'}),
        label='password')
    
class SignupForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__name_input',
            'placeholder': 'First Name',
            'type': 'text' }),
        label='firstname')
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__name_input',
            'placeholder': 'Last Name',
            'type': 'text' }),
        label='lastname')
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__input',
            'placeholder': 'Enter Username',
            'type': 'text' }),
        label='username',
        max_length=20)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'signup__input',
            'placeholder': 'Enter Email',
            'type': 'email'}),
        label='email')
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__input',
            'placeholder': 'Enter Password',
            'type': 'password'}),
        label='password')
    confirmpassword = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__input',
            'placeholder': 'Re-Enter Password',
            'type': 'password'}),
        label='confirmpassword')
    
    def clean(self):
        cd = self.cleaned_data
        password = cd.get("password")
        confirmpassword = cd.get("confirmpassword")

        if password != confirmpassword:
            raise ValidationError('Passwords do not match',  code='mismatch')
