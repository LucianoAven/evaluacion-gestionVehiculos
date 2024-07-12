# Método List para listar la cantidad de elementos que se filtren y método Optional
# para especificar el valor que retorne en caso de que la variable no reciba información.
from typing import List, Optional

# Importo los modelos de las columnas que poseen las tablas de la base de datos.
from vehiculos.models import Pais

# Funciones para las distintas acciones de la página.
class PaisRepository:

    # Visualizar todas los elementos almacenados.
    def get_all(self) -> List[Pais]:
        return Pais.objects.all()

    # Buscar un elemento por su id.
    def filter_by_id(self, id: int) -> Optional[Pais]:
        # Retorna el elemento con la id espicificada en la función.
        return Pais.objects.filter(id=id).first()

    # Muestra el elemento con la id especificada.    
    def get_by_id(self, id: int) -> Optional[Pais]:
        # Envía un componente vacío en caso de no haber un elemento con la id ingresada.
        try:
            pais = Pais.objects.get(id=id)
        except:
            pais = None
        return pais

    # Modifico un elemento de la lista.
    def update(self, pais: Pais, nombre: str):

        # Reemplazo las caracteristicas anteriores por las nuevas realizadas.
        pais.name = nombre

        # Guardo las actualizaciones realizadas para que se mantengan una vez se cierre la página.
        pais.save()

    # Agrega un nuevo elemento.
    def create(self, nombre: str) -> Pais:
        
        pais = Pais.objects.filter(name=nombre)

        if pais:
            return "El país ya se encuentra en la lista"

        return Pais.objects.create(
            name=nombre,
        )