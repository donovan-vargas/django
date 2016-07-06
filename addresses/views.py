# coding=utf-8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import AddAddress, UpdateAddress
from .models import Addresses


# Create your views here.
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
            user_address = Addresses()
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
    addresses = Addresses.objects.filter(user=request.user)
    context_address = {
        'addresses': addresses
    }
    return render(request, 'addresses/agregar_direccion.html', {'form': form,
                                                                'addresses': addresses})


@login_required
def edit_address_view(request, pk):
    if request.method == 'POST':
        form = UpdateAddress(request.POST)
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
            user_address = Addresses(pk)
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
        addresses = Addresses.objects.get(pk=pk)
        form = AddAddress(initial={'state': addresses.state,
                                   'city': addresses.city,
                                   'suburb': addresses.suburb,
                                   'postal_code': addresses.postal_code,
                                   'street': addresses.street,
                                   'number': addresses.number,
                                   'crossing_x': addresses.crossing_x,
                                   'crossing_y': addresses.crossing_y,})

    return render(request, 'addresses/editar_direccion.html', {'form': form})
