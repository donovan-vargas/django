from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone


# Create your views here.
def index_view(request):
    context = {
        'ahora': timezone.now()
    }
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
        mensaje = 'Nombre de usuario o password no valido'
    return render(request, 'home/index.html', context)
    # return render(request, 'home/index.html', context)
