from django import forms

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
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'signup__input',
            'placeholder': 'Enter Username',
            'type': 'text' }),
        label='username',
        max_length=20)
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
        label='confirmpassword'
    )