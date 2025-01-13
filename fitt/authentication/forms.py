from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError

class signup_form(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    

class login_form(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs = {
                "autofocus": True,
                'class': 'login__input',
                'placeholder': 'Enter Username',
                'type': 'text'
            }),
        label='username'
    )

    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'login__input',
            'placeholder': 'Enter Password',
            'type': 'password'}),
        label='password')
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
class SignupForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__input',
            'placeholder': 'First Name',
            'type': 'text' }),
        label='firstname')
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__input',
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
