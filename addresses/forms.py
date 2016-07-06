# coding=utf-8
from django import forms


from .models import StatesCatalog, SuburbCatalog, PostalCodeCatalog, CitiesCatalog
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


class UpdateAddress(forms.Form):
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