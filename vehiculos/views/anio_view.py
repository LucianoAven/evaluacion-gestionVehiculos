from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from vehiculos.repositories.anio import AnioRepository
from vehiculos.repositories.auto import AutoRepository

repoY = AnioRepository()
repoA = AutoRepository()

def anio_list(request):
    anios = repoY.get_all()

    return render(
        request,
        'anios/list.html',
        dict(
            years=anios
        )
    )

def anio_detail(request, id:int):

    anio = repoY.filter_by_id(id)
    autos = repoA.filter_by_anio(anio)

    return render(
        request,
        'anios/detail.html',
        dict (
            year = anio,
            cars = autos,
        )
    )

