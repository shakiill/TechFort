from django.forms import ModelForm
from django import forms
from .models import User, Profile

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# forms

class ProfileForm(ModelForm):
    # print(ModelForm.)
    firstname = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={'id': "firstname", 'placeholder': "First Name", 'name': "firstname", 'value': ""}, ),
    )
    lastname = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={'id': "lastname", 'placeholder': "Last Name", 'name': "lastname", 'value': ""}, ),
    )
    phone = forms.CharField(
        label="Mobile",
        widget=forms.TextInput(
            attrs={'id': "phone", 'placeholder': "", 'name': "phone", 'value': ""}, ),
    )
    email = forms.CharField(
        label="Email",
        widget=forms.TextInput(
            attrs={'id': "email", 'placeholder': "", 'name': "email", 'value': ""}, ),
    )
    address_1 = forms.CharField(
        label="Address",
        widget=forms.TextInput(
            attrs={'id': "address_1", 'placeholder': "", 'name': "address_1", 'value': ""}, ),
    )

    class Meta:
        model = Profile
        fields = ('firstname', 'lastname', 'phone', 'email', 'address_1')
        # widgets = {
        #     'lastname': forms.TextInput(
        #         attrs={'id': "lastname", 'placeholder': "Enter your last name", 'name': "lastname"}),
        #     'address_1': forms.Textarea(
        #         attrs={'id': "address_1", 'placeholder': "Enter your full address", 'name': "address_1"}),
        # }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'id': 'c-password', 'placeholder': 'Enter password',
                   'data-toggle': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'id': 'newpassword', 'placeholder': 'Re-type password',
                   'data-toggle': 'password'}),
    )

    class Meta:
        model = User
        fields = ('first_name', 'phone', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'f-name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'required': ''}),
            # 'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'newpassword', 'required': ''}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'c-password', 'required': ''}),
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'required': '',
                                               'name': 'username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password',
                                                   'required': '', 'name': 'password'}),
        }