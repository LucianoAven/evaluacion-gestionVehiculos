# Método List para listar la cantidad de elementos que se filtren y método Optional
# para especificar el valor que retorne en caso de que la variable no reciba información.
from typing import List, Optional

# Importo los modelos de las columnas que poseen las tablas de las marcas de autos.
from vehiculos.models import Marca


#logger = logging.getLogger(__name__)

# Funciones para las distintas acciones de la página.
class MarcaRepository:

    # Visualizar todas las marcas almacenadas.
    def get_all(self) -> List[Marca]:
        return Marca.objects.all()

    # Buscar un marca de auto por su id.
    def filter_by_id(self, id: int) -> Optional[Marca]:
        # Retorna la marca con la id espicificada en la función.
        return Marca.objects.filter(id=id).first()

    # Muestra el la marca con la id especificada.    
    def get_by_id(self, id: int) -> Optional[Marca]:
        # Envía un componente vacío en caso de no haber un elemento con la id ingresada.
        try:
            marca = Marca.objects.get(id=id)
        except:
            marca = None
        return marca

    # Eliminar una marca de auto
    def delete(self, marca: Marca):
        return marca.delete()

    # Modifico una marca de autos de la lista.
    def update(self, marca: Marca, nombre: str):

        # Reemplazo las caracteristicas anteriores por las nuevas realizadas.
        marca.name = nombre

        # Guardo las actualizaciones realizadas para que se mantengan una vez se cierre la página.
        marca.save()

    # Agrega una nueva marca de autos.
    def create(self, nombre: str) -> Marca:    
        
        marca = Marca.objects.filter(name=nombre)

        if marca:
            return "La marca de auto ya se encuentra en la lista"

        return Marca.objects.create(
            name=nombre,
        )