from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from vehiculos.forms import MarcaForm

from vehiculos.repositories.marca import MarcaRepository
from vehiculos.repositories.auto import AutoRepository

repoM = MarcaRepository()

def marca_list(request):
    marcas = repoM.get_all()

    return render(
        request,
        'marcas/list.html',
        dict(
            marcas=marcas
        )
    )

# Permite al usuario crear una nueva marca de autos
def marca_create(request):

    if request.method == "POST":

        # Habilito al usuario agregar una nueva marca de autos desde la parte externa del sitio web.
        nombre = request.POST.get('name')

        # Establezco la nueva marca con su respectiva función del repositorio.
        repoM.create(
            nombre = nombre,
        )

        # Redirecciona a la función de detalles para ver el resultado del nuevo elemento.
        return redirect('marca_list')

    # Vinculo la función con el archivo html que permite añadir marcas de autos desde el sitio web html.
    return render(
        request,
        'marcas/create.html',
    )

# Actualiza el nombre de una marca.
def marca_update(request, id:int):

    # Almacena la marca que quiero modificar
    marca = repoM.get_by_id(id)

    if request.method == "POST":

        # Habilito la modificación del contenido de las columnas en HTML.
        name = request.POST.get('name')

        # Utilizo la función para actualizar del repositorio para reemplazar las anteriores columnas
        # por las nuevas.
        repoM.update(
            marca = marca,
            nombre = name,
        )

        # Redirijo el resultado a la función para ver las modificaciones.
        return redirect('marca_detail', marca.id)

    # Vínculo la función con el archivo Html que habilita a los usuarios modificar las columnas.
    return render(
        request,
        'marcas/update.html',
        dict(
            marca=marca,
        )
    )

# Muestra los detalles de una marca en específico
def marca_detail(request, id:int):

    repoM = MarcaRepository()
    repoA = AutoRepository()

    marca = repoM.get_by_id(id)
    autos = repoA.filter_by_mark(marca)

    return render(
        request,
        'marcas/detail.html',
        dict (
            mark = marca,
            cars = autos,
        )
    )
