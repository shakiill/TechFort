from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

# Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Forms and Models
from django.views.generic import CreateView

from .models import Profile
from .forms import ProfileForm, SignUpForm, LoginForm
from .models import User

# Messages
from django.contrib import messages


# Create your views here.


# def home(request):
#     return render(request, 'home.html')


# def sign_up(request):
#     form = SignUpForm()
#     if request.method == 'POST':
#         print("start")
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             print("success")
#             form.save()
#             messages.success(request, "Account Created Successfully!")
#             return HttpResponseRedirect(reverse('account:login'))
#         elif form.password1 != form.password2:
#             error_msg = {'Passwords are not same'}
#             return render(request, 'account/register.html', context={'form': form, 'error_msg': error_msg})
#     return render(request, 'account/register.html', context={'form': form})


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.save()
            print("valid")
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return HttpResponseRedirect(reverse('App_Auth:login'))
            # return render(request, 'account/login.html', context=context)
        elif not form.is_valid():
            messages.error(request, form.error_messages)
            print(form.error_messages)
            return render( request, 'App_Auth/register.html', context={'form': form} )
    # return HttpResponseRedirect("/signup/")
    return render( request, 'App_Auth/register.html', context={'form': form} )


def login_user(request):
    # form = AuthenticationForm()
    form = LoginForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in.")
                return render( request, 'home.html' )
    # return HttpResponseRedirect(reverse('account:login'))
    return render( request, 'App_Auth/login.html', context={'form': form} )


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You have been logged out!")
    return HttpResponseRedirect(reverse('products:home'))
    # return render(request, 'home.html')


@login_required
def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    # form.fields['username'].widget.attrs['placeholder'] = profile.user
    form.fields['firstname'].widget.attrs['placeholder'] = profile.user.first_name
    if form.fields['firstname'].widget.attrs['value'] != "":
        form.fields['firstname'].widget.attrs['value'] = profile.user.first_name
    form.fields['phone'].widget.attrs['placeholder'] = profile.user.phone
    if form.fields['phone'].widget.attrs['value'] != "":
        form.fields['phone'].widget.attrs['value'] = profile.user.phone
    form.fields['email'].widget.attrs['placeholder'] = profile.user.email
    if form.fields['email'].widget.attrs['value'] != "":
        form.fields['email'].widget.attrs['value'] = profile.user.email
    form.fields['lastname'].widget.attrs['placeholder'] = profile.lastname
    if form.fields['lastname'].widget.attrs['value'] != "":
        form.fields['lastname'].widget.attrs['value'] = profile.user.lastname
    # form.fields['phone'].widget.attrs['placeholder'] = profile.firstname
    form.fields['address_1'].widget.attrs['placeholder'] = profile.address_1
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        form.save()
        return render( request, 'App_Auth/myAccountScreen.html',
                       context={'form': form} )

    return render( request, 'App_Auth/myAccountScreen.html',
                   context={'form': form} )


def forgot_pass(request):
    return render( request, 'App_Auth/forgot-password.html' )