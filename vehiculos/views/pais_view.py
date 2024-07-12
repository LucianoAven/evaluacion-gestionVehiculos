from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from vehiculos.forms import PaisForm

from vehiculos.repositories.pais import PaisRepository
from vehiculos.repositories.auto import AutoRepository

repoP = PaisRepository()

def pais_list(request):
    paises = repoP.get_all()

    return render(
        request,
        'paises/list.html',
        dict(
            countries=paises
        )
    )

# Permite al usuario crear un nuevo elemento.
def pais_create(request):

    if request.method == "POST":

        # Habilito al usuario agregar un nuevo elemento desde la parte externa del sitio web.
        nombre = request.POST.get('name')

        # Establezco el nuevo elemento con su respectiva función del repositorio.
        repoP.create(
            nombre = nombre,
        )

        # Redirecciona a la función de detalles para ver el resultado del nuevo elemento.
        return redirect('pais_list')

    # Vinculo la función con el archivo html que permite añadir el nuevo elemento desde el sitio web html.
    return render(
        request,
        'paises/create.html',
    )

# Actualiza el nombre del elemento.
def pais_update(request, id:int):

    # Almacena el elemento que quiero modificar
    pais = repoP.get_by_id(id)

    if request.method == "POST":

        # Habilito la modificación del contenido de las columnas en HTML.
        name = request.POST.get('name')

        # Utilizo la función para actualizar del repositorio para reemplazar las anteriores columnas
        # por las nuevas.
        repoP.update(
            pais = pais,
            nombre = name,
        )

        # Redirijo el resultado a la función para ver las modificaciones.
        return redirect('pais_detail', pais.id)

    # Vínculo la función con el archivo Html que habilita a los usuarios modificar las columnas.
    return render(
        request,
        'paises/update.html',
        dict(
            country=pais,
        )
    )

# Muestra los detalles de un elemento en específico
def pais_detail(request, id:int):

    repoA = AutoRepository()

    pais = repoP.get_by_id(id)
    autos = repoA.filter_by_country(pais)

    return render(
        request,
        'paises/detail.html',
        dict (
            country = pais,
            cars = autos,
        )
    )
