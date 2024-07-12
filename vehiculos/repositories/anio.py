# Método List para listar la cantidad de elementos que se filtren y método Optional
# para especificar el valor que retorne en caso de que la variable no reciba información.
from typing import List, Optional

# Importo los modelos de las columnas que poseen las tablas de Auto.
from vehiculos.models import Anio

# Funciones para las distintas acciones de la página.
class AnioRepository:

    # Visualizar todos los elementos almacenados.
    def get_all(self) -> List[Anio]:

        total_columnas = Anio.objects.exclude(name=True).count()

        contador = 1960

        # Asegura que no se vuelvan a rellenar las celdas si ya poseen infromación
        if total_columnas == 0:
            for x in range(64):
                Anio.objects.create(
                    name=contador,
                )
                contador += 1

        return Anio.objects.all()

    # Buscar un producto por su id.
    def filter_by_id(self, id: int) -> Optional[Anio]:
        # Retorna el elemento con la id espicificada en la función.
        return Anio.objects.filter(id=id).first()
