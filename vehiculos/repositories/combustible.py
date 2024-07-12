# Método List para listar la cantidad de elementos que se filtren y método Optional
# para especificar el valor que retorne en caso de que la variable no reciba información.
from typing import List, Optional

# Importo los modelos de las columnas que poseen las tablas de la base de datos.
from vehiculos.models import Combustible

# Funciones para las distintas acciones de la página.
class CombustibleRepository:

    # Visualizar todas los elementos almacenados.
    def get_all(self) -> List[Combustible]:
        return Combustible.objects.all()

    # Buscar un elemento por su id.
    def filter_by_id(self, id: int) -> Optional[Combustible]:
        # Retorna el elemento con la id espicificada en la función.
        return Combustible.objects.filter(id=id).first()

    # Muestra el elemento con la id especificada.    
    def get_by_id(self, id: int) -> Optional[Combustible]:
        # Envía un componente vacío en caso de no haber un elemento con la id ingresada.
        try:
            combustible = Combustible.objects.get(id=id)
        except:
            combustible = None
        return combustible

    # Modifico un elemento de la lista.
    def update(self, combustible: Combustible, nombre: str):

        # Reemplazo las caracteristicas anteriores por las nuevas realizadas.
        combustible.name = nombre

        # Guardo las actualizaciones realizadas para que se mantengan una vez se cierre la página.
        combustible.save()

    # Agrega un nuevo elemento.
    def create(self, nombre: str) -> Combustible:
        
        combustible = Combustible.objects.filter(name=nombre)

        if combustible:
            return "El tipo de combustible ya se encuentra incluido en la lista"

        return Combustible.objects.create(
            name=nombre,
        )