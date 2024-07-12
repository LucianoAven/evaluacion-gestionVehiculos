from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from vehiculos.forms import CombustibleForm

from vehiculos.repositories.combustible import CombustibleRepository
from vehiculos.repositories.auto import AutoRepository

repoC = CombustibleRepository()

def combustible_list(request):
    combustibles = repoC.get_all()

    return render(
        request,
        'combustibles/list.html',
        dict(
            fuels=combustibles
        )
    )

# Permite al usuario crear un nuevo elemento.
def combustible_create(request):

    if request.method == "POST":

        # Habilito al usuario agregar un nuevo elemento desde la parte externa del sitio web.
        nombre = request.POST.get('name')

        # Establezco el nuevo elemento con su respectiva función del repositorio.
        repoC.create(
            nombre = nombre,
        )

        # Redirecciona a la función de detalles para ver el resultado del nuevo elemento.
        return redirect('combustible_list')

    # Vinculo la función con el archivo html que permite añadir el nuevo elemento desde el sitio web html.
    return render(
        request,
        'combustibles/create.html',
    )

# Actualiza el nombre del elemento.
def combustible_update(request, id:int):

    # Almacena el elemento que quiero modificar
    combustible = repoC.get_by_id(id)

    if request.method == "POST":

        # Habilito la modificación del contenido de las columnas en HTML.
        name = request.POST.get('name')

        # Utilizo la función para actualizar del repositorio para reemplazar las anteriores columnas
        # por las nuevas.
        repoC.update(
            combustible = combustible,
            nombre = name,
        )

        # Redirijo el resultado a la función para ver las modificaciones.
        return redirect('combustible_detail', combustible.id)

    # Vínculo la función con el archivo Html que habilita a los usuarios modificar las columnas.
    return render(
        request,
        'combustibles/update.html',
        dict(
            fuel=combustible,
        )
    )

# Muestra los detalles de un elemento en específico
def combustible_detail(request, id:int):

    repoA = AutoRepository()

    combustible = repoC.get_by_id(id)
    autos = repoA.filter_by_fuel(combustible)

    return render(
        request,
        'combustibles/detail.html',
        dict (
            fuel = combustible,
            cars = autos,
        )
    )
