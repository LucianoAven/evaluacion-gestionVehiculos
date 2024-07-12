from django.urls import path

# Importo las funciones de las vistas para vincularlas con los archivos html.
from vehiculos.views.auto_view import (
    auto_list,
    auto_create,
    auto_detail,
    auto_update,
    auto_delete,
)

from vehiculos.views.marca_view import (
    marca_list,
    marca_create,
    marca_detail,
    marca_update,
)

from vehiculos.views.anio_view import (
    anio_list,
    anio_detail,
)

from vehiculos.views.combustible_view import (
    combustible_list,
    combustible_create,
    combustible_detail,
    combustible_update,
)

from vehiculos.views.pais_view import (
    pais_list,
    pais_create,
    pais_detail,
    pais_update,
)

urlpatterns = [

    # Especifico las rutas donde se visualizaran los archivos html con sus funciones.
    path(route='', view=auto_list, name="auto_list"),
    path(route='create/',view=auto_create, name='auto_create'),
    path(route='<int:id>/',view=auto_detail,name="auto_detail"),
    path(route='<int:id>/update/',view=auto_update,name="auto_update"),
    path(route='<int:id>/delete/', view=auto_delete, name="auto_delete"),

    # Rutas de las marcas de autos
    path(route='marca/', view=marca_list, name="marca_list"),
    path(route='marca/create/',view=marca_create, name='marca_create'),
    path(route='marca/<int:id>/',view=marca_detail,name="marca_detail"),
    path(route='marca/<int:id>/update/',view=marca_update,name="marca_update"),

    # Rutas de los combustibles de autos.
    path(route='combustible/', view=combustible_list, name="combustible_list"),
    path(route='combustible/create/',view=combustible_create, name='combustible_create'),
    path(route='combustible/<int:id>/',view=combustible_detail,name="combustible_detail"),
    path(route='combustible/<int:id>/update/',view=combustible_update,name="combustible_update"),

    # Rutas de los paises de fabricación.
    path(route='pais/', view=pais_list, name="pais_list"),
    path(route='pais/create/',view=pais_create, name='pais_create'),
    path(route='pais/<int:id>/',view=pais_detail,name="pais_detail"),
    path(route='pais/<int:id>/update/',view=pais_update,name="pais_update"),

    # Rutas de los años de fabricación.
    path(route='anio/', view=anio_list, name="anio_list"),
    path(route='anio/<int:id>', view=anio_detail, name="anio_detail"),

]