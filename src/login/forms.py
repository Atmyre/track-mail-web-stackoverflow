# coding: utf-8

from .models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        ordering = ('-date_joined', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()
        verbose_name = u'Профиль'
        verbose_name_plural = u'Профили'
        ordering = ('-user.date_joined', )
