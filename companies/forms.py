# coding=utf-8
from django import forms
from django.contrib.auth.models import User


class RegistrerCompaniesForm(forms.Form):
    company = forms.CharField(
        min_length=3,
        label='Nombre de la compañía',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirme password',
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registrado')
        return email

    def clean_password2(self):
        """Comprueba que el password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Los passwords no coinciden')
        return password2
