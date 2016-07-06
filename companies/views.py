# coding=utf-8
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail.message import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import RegistrerCompaniesForm
from .models import CompanyUser

def register_company_view(request):
    """Registro de compañias"""
    if request.method == 'POST':
        form = RegistrerCompaniesForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('email')
            company = cleaned_data.get('company')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            # instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username,
                                                  password=password,
                                                  first_name=company)
            user_model.email = email
            user_model.save()
            company_user = CompanyUser()
            company_user.company = user_model
            company_user.save()
            asunto = 'Servifeng'
            mens = 'Se a realizado su registro correctamente su usuario es: ' + username
            mens = mens + r' ingrese a http://127.0.0.1:8000/admin/'
            mail = EmailMessage(asunto, mens, to=[email, 'servifeng@gmail.com'])
            mail.send()
            return redirect(reverse('accounts.gracias', kwargs={'username': username}))
    else:
        form = RegistrerCompaniesForm()

    context ={
        'form': form
    }
    return render(request, 'companies/registro.html', context)

