from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

# Genera las funciones para el inicio de sesión y las mostra por pantalla.
class LoginView(View):

    def get(self, request):
        return render(
            request,
            'home/login.html',
        )

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')

# Genera las funciones para el cierre de sesión.
class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')

# Archivo HTML donde se recopilarán las distintas categorías para filtrar los autos.
def filters(request):
    return render(
        request,
        'home/filtros.html',
    )

# Realiza una acción según si el usuario se encuentra logeado.
@login_required(login_url='login')
# Diseña la vista del sitio principal.
def index_view(request):
    return render(
        # Corre el html que diseña la vista principal.
        request,
        'home/index.html',
    )