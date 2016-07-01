# coding=utf-8
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail.message import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import RegisterUserForm, EditEmailForm, EditPasswordForm, EditPhoto, AddAddress, UpdateUserAddress
from .models import UserProfile, UserAddress


# Create your views here.


@login_required
def index_view(request):
    # Si el usuario ya esta logueado, lo direccionamos a index_view
    return render(request, 'accounts/index.html')


def login_view(request):
    """Valida el acceso del usuario"""
    # Si el usuario ya esta logueado, lo direccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('accounts.index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('accounts.index'))
            else:
                # direccionar informando que la cuenta esta inactiva
                mensaje = 'La cuenta se encuentra inactva'
                return render(request, 'accounts/login.html', {'mensaje': mensaje})
        mensaje = 'Nombre de usuario o contraseña no valido'
    return render(request, 'accounts/login.html', {'mensaje': mensaje})


def register_user_view(request):
    """Registro de usuarios"""
    if request.method == 'POST':
        # Si el metodo es post, obtenemos datos del formulario
        form = RegisterUserForm(request.POST, request.FILES)

        # Comprobamos si el formulario es vacio
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('email')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            photo = cleaned_data.get('photo')
            # instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username,
                                                  password=password,
                                                  first_name=first_name,
                                                  last_name=last_name)
            # agregamos email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # y le asignamos la photo(el campo permite datos null)
            user_profile.photo = photo
            # damos valor de servicios y escore por defecto
            user_profile.services = 0
            user_profile.score = 0.0
            # Por ultimo, guardamos también el objeto UserProfile
            user_profile.save()
            # Ahora direccionaremos a la pagina accounts/gracias.html
            # Pero lo hacemos con un redirect.
            asunto = 'Servifeng'
            mens = 'Se a realizado su registro correctamente su usuario es: ' + username
            mens = mens + r' ingrese a http://127.0.0.1:8000/accounts/'
            mail = EmailMessage(asunto, mens, to=[email, 'servifeng@gmail.com'])
            mail.send()
            return redirect(reverse('accounts.gracias', kwargs={'username': username}))
    else:
        # si el método es GET, instanciamos un objeto RegisterUserForm vacio
        form = RegisterUserForm()
    # Creamos el contexto
    context = {
        'form': form
    }
    # Y mostramos los datos
    return render(request, 'accounts/registro.html', context)


def thanks_view(request, username):
    # Pantalla de agradecimiento por el registro
    return render(request, 'accounts/gracias.html', {'username': username})


def logout_view(request):
    """Desconecta de la aplicacion"""
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect(reverse('accounts.login'))


@login_required
def edit_email_view(request):
    """Editar email del usuario"""
    # Si el método es post, obtenemos datos del formulario
    if request.method == 'POST':
        form = EditEmailForm(request.POST, request=request)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, 'El email ha sido cambiado con exito!.')
            return redirect(reverse('accounts.index'))
    else:
        form = EditEmailForm(request=request, initial={'email': request.user.email})
    return render(request, 'accounts/editar_email.html', {'form': form})


@login_required
def edit_password_view(request):
    """Editar el password"""
    # Si el método es post, obtenemos datos del formulario
    if request.method == 'POST':
        form = EditPasswordForm(request.POST)
        if form.is_valid():
            username = request.user.username
            user = authenticate(username=username, password=form.cleaned_data['password_now'])
            if user is None:
                messages.error(request, 'La contraseña actual no coincide')
                return redirect(reverse('accounts.editar_contrasena'))
            request.user.password = make_password(form.cleaned_data['password'])
            request.user.save()
            messages.success(request, 'El password ha sido cambiado con exito!.')
            messages.success(request, 'Es necesario introducir los datos para entrar.')
            return redirect(reverse('accounts.index'))
    else:
        form = EditPasswordForm()
    return render(request, 'accounts/editar_contrasena.html', {'form': form})


@login_required
def edit_photo_view(request):
    """Editar imagen del usuario"""
    if request.method == 'POST':
        form = EditPhoto(request.POST, request.FILES)
        if form.is_valid():
            user_profile = UserProfile.objects.get(pk=request.user.id)
            user_profile.photo.delete()
            user_profile.photo = form.cleaned_data['photo']
            user_profile.save()
            messages.success(request, 'La imagen ha sido cambiada con exito!.')
            return redirect(reverse('accounts.index'))
    else:
        form = EditPhoto()
    return render(request, 'accounts/editar_foto.html', {'form': form})


@login_required
def add_address_view(request):
    if request.method == 'POST':
        form = AddAddress(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            state = clean_data.get('state')
            city = clean_data.get('city')
            suburb = clean_data.get('suburb')
            postal_code = clean_data.get('postal_code')
            street = clean_data.get('street')
            number = clean_data.get('number')
            crossing_x = clean_data.get('crossing_x')
            crossing_y = clean_data.get('crossing_y')
            user_address = UserAddress()
            user_address.state = state
            user_address.city = city
            user_address.suburb = suburb
            user_address.postal_code = postal_code
            user_address.street = street
            user_address.number = number
            user_address.crossing_x = crossing_x
            user_address.crossing_y = crossing_y
            user_address.user = request.user
            user_address.save()
            messages.success(request, 'Dirección guardada con éxito')
            return redirect(reverse('accounts.index'))
    else:
        form = AddAddress()
    addresses = UserAddress.objects.filter(user=request.user)
    context_address = {
        'addresses': addresses
    }
    return render(request, 'accounts/agregar_direccion.html', {'form': form,
                                                               'addresses': addresses})


@login_required
def edit_address_view(request, pk):
    if request.method == 'POST':
        form = UpdateUserAddress(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            state = clean_data.get('state')
            city = clean_data.get('city')
            suburb = clean_data.get('suburb')
            postal_code = clean_data.get('postal_code')
            street = clean_data.get('street')
            number = clean_data.get('number')
            crossing_x = clean_data.get('crossing_x')
            crossing_y = clean_data.get('crossing_y')
            user_address = UserAddress(pk)
            user_address.state = state
            user_address.city = city
            user_address.suburb = suburb
            user_address.postal_code = postal_code
            user_address.street = street
            user_address.number = number
            user_address.crossing_x = crossing_x
            user_address.crossing_y = crossing_y
            user_address.user = request.user
            user_address.save()
            messages.success(request, 'Dirección actualizada con éxito')
            return redirect(reverse('accounts.index'))
    else:
        addresses = UserAddress.objects.get(pk=pk)
        form = AddAddress(initial={'state': addresses.state,
                                   'city': addresses.city,
                                   'suburb': addresses.suburb,
                                   'postal_code': addresses.postal_code,
                                   'street': addresses.street,
                                   'number': addresses.number,
                                   'crossing_x': addresses.crossing_x,
                                   'crossing_y': addresses.crossing_y,})

    return render(request, 'accounts/editar_direccion.html', {'form': form})
