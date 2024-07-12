from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Importa el modelo de la tabla Categoría.
from vehiculos.models import Marca, Anio, Combustible, Pais
from vehiculos.forms import AutoForm

from vehiculos.repositories.auto import AutoRepository

# Almaceno en una variable la clase contiene todas las funciones para interactuar con
# la base de datos.
repoA = AutoRepository()

# Permite visualizar y enlistar todos los autos disponibles.
def auto_list(request):
    autos = repoA.get_all()
    # Vínculo la función para ver todos los modelos con el archivo html que posee 
    # el diseño de la página principal.
    return render(
        request,
        'autos/list.html',
        # Cambio la variable que recorrerá el for por la variable que posee la tabla de autos. 
        dict(
            cars=autos
        )
    )

# Muestra los detalles del elemento seleccionado.
def auto_detail(request, id):
    auto = repoA.get_by_id(id=id)
    # Vincula la funcíon para ver los detalles de un elemento con el html que permite
    # visualizarlos mejor.
    return render(
        request,
        'autos/detail.html',
        {"auto":auto}
    )

# Crear un nuevo producto.
def auto_create(request):
    form = AutoForm(request.POST)

    if request.method == "POST":

        if form.is_valid():
            # Creo la nueva tabla con la función del repositorio.
            auto_nuevo = repoA.create(
                nombre = form.cleaned_data['name'],
                marca = form.cleaned_data['mark'],
                precio = form.cleaned_data['price'],
                anio = form.cleaned_data['year'],
                combustible = form.cleaned_data['fuel'],
                pais = form.cleaned_data['country'],
            )
            return redirect('auto_detail', auto_nuevo.id)

    # Variable almacenando repositorio de base de datos.
    marcas = Marca.objects.all()
    return render (
        request, 
        'autos/create.html',
        {'form':form}
    )

@login_required(login_url='login')
def auto_update(request, id):
    # Almaceno el elemento que quiero modificar
    car = repoA.get_by_id(id=id)

    # Almaceno todas las categorías de la tabla.
    marcas = Marca.objects.all()
    anios = Anio.objects.all()
    combustibles = Combustible.objects.all()
    paises = Pais.objects.all()

    if request.method == "POST":

        # Habilito la modificación del contenido de las columnas en HTML.
        name = request.POST.get('name')
        id_mark = request.POST.get('id_mark')
        price = request.POST.get('price')
        id_year = request.POST.get('id_year')
        id_fuel = request.POST.get('id_fuel')
        id_country = request.POST.get('id_country')

        if id_mark:
            mark = Marca.objects.get(id=id_mark)
        else:
            mark = None

        if id_year:
            year = Anio.objects.get(id=id_year)
        else:
            year = None

        if id_fuel:
            fuel = Combustible.objects.get(id=id_fuel)
        else:
            fuel = None

        if id_country:
            country = Pais.objects.get(id=id_country)
        else:
            country = None

        # Utilizo la función para actualizar del model para reemplazar las anteriores columnas
        # por las nuevas.
        repoA.update(
            auto = car,
            nombre = name,
            marca = mark,
            precio = price,
            anio = year,
            combustible = fuel,
            pais = country,
        )

        # Redirijo el resultado a la función de ver detalles para revisar las modificaciones
        return redirect('auto_detail', car.id)

    # Vínculo la función con el archivo Html que habilita a los usuarios modificar las columnas.
    return render(
        request,
        'autos/update.html',
        dict(
            marks=marcas,
            years=anios,
            fuels=combustibles,
            countries=paises,
            auto=car,
        )
    )

# Elimino un producto y vuelvo a rehacer toda la lista redirrigiendo la función a product_detail.
def auto_delete(request, id):
    car = repoA.get_by_id(id=id)
    repoA.delete(auto=car)
    # Nombre del listado de productos en la url.
    return redirect('auto_list')
