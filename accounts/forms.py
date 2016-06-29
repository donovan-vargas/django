# coding=utf-8
from django import forms
from django.contrib.auth.models import User

from .models import StatesCatalog, SuburbCatalog, PostalCodeCatalog, CitiesCatalog


class EditPasswordForm(forms.Form):
    password_now = forms.CharField(
        label='Contraseña actual',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label='Nueva contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Repetir contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean_password2(self):
        """Comprueba que el password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2


class EditPhoto(forms.Form):
    """Editar imagen del perfil"""
    photo = forms.ImageField()


class EditEmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        """Obtener request"""
        self.request = kwargs.pop('request')
        super(EditEmailForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        # Comprobar si ha cambiado email
        email_now = self.request.user.email
        username = self.request.user.username
        if email != email_now:
            # Si lo a cambiado, comprobar que no exista en la db.
            # Excluye el usuario actual
            exist = User.objects.filter(email=email).exclude(username=username)
            if exist:
                raise forms.ValidationError('Ya existe un email igual registrado')
        return email


class RegisterUserForm(forms.Form):
    first_name = forms.CharField(
        min_length=5,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        min_length=5,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    """username = forms.CharField(
        min_length=5,
        label='Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )"""
    email = forms.EmailField(
        label='Correo electronico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirme password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    photo = forms.ImageField(required=False)

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registrado.')
        return email

    def clean_password2(self):
        """Comprueba que el password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2


class AddAddress(forms.Form):
    state = forms.ModelChoiceField(
        queryset=StatesCatalog.objects.all().order_by('state'),
        label='Estado',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    city = forms.ModelChoiceField(
        queryset=CitiesCatalog.objects.all().order_by('city'),
        label='Ciudad',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    suburb = forms.ModelChoiceField(
        queryset=SuburbCatalog.objects.all().order_by('suburb'),
        label='Colonia',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    postal_code = forms.ModelChoiceField(
        queryset=PostalCodeCatalog.objects.all().order_by('postal_code'),
        label='Código Postal',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    street = forms.CharField(
        min_length=1,
        label='Calle',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    number = forms.CharField(
        min_length=1,
        label='Numero',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    crossing_x = forms.CharField(
        required=False,
        label='Cruce',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    crossing_y = forms.CharField(
        required=False,
        label='Cruce',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class UpdateUserAddress(forms.Form):
    state = forms.ModelChoiceField(
        queryset=StatesCatalog.objects.all().order_by('state'),
        label='Estado',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    city = forms.ModelChoiceField(
        queryset=CitiesCatalog.objects.all().order_by('city'),
        label='Ciudad',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    suburb = forms.ModelChoiceField(
        queryset=SuburbCatalog.objects.all().order_by('suburb'),
        label='Colonia',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    postal_code = forms.ModelChoiceField(
        queryset=PostalCodeCatalog.objects.all().order_by('postal_code'),
        label='Código Postal',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    street = forms.CharField(
        min_length=1,
        label='Calle',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    number = forms.CharField(
        min_length=1,
        label='Numero',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    crossing_x = forms.CharField(
        required=False,
        label='Cruce',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    crossing_y = forms.CharField(
        required=False,
        label='Cruce',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
