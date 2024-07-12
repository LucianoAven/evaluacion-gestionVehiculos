# Método List para listar la cantidad de elementos que se filtren y método Optional
# para especificar el valor que retorne en caso de que la variable no reciba información.
from typing import List, Optional

# Importo los modelos de las columnas que poseen las tablas de Auto.
from vehiculos.models import Auto, Marca, Anio, Combustible, Pais


#logger = logging.getLogger(__name__)

# Funciones para las distintas acciones de la página.
class AutoRepository:

    # Visualizar todos los autos almacenados.
    def get_all(self) -> List[Auto]:
        return Auto.objects.all()

    # Buscar un producto por su id.
    def filter_by_id(self, id: int) -> Optional[Auto]:
        # Retorna el elemento con la id espicificada en la función.
        return Auto.objects.filter(id=id).first()

    # Muestra el elemento con la id especificada.    
    def get_by_id(self, id: int) -> Optional[Auto]:
        # Envía un componente vacío en caso de no haber un elemento con la id ingresada.
        try:
            auto = Auto.objects.get(id=id)
        except:
            auto = None
        return auto

    # Filtra todos los Autos cuyo valor se encuentre entre los precios especificados.
    def filter_car_on_price_range(
        self,
        min_price: float,
        max_price: float,

    ) -> List[Auto]:

        autos = Auto.objects.filter(
            price__range=(min_price, max_price)
        )

        return autos

    # Crea un nuevo elemento y especifica sus características.
    def create(
        self,
        nombre: str,
        precio: float,
        marca: Optional[Marca] = None,
        anio: Optional[Anio] = None,
        combustible: Optional[Combustible] = None,
        pais: Optional[Pais] = None,
    ):
        return Auto.objects.create(
            # Agrego los datos ingresados del nuevo elemento en las columnas de la tabla.
            name=nombre,
            mark=marca,
            price=precio,
            year=anio,
            fuel=combustible,
            country=pais,
        )

    # Filtrar los productos que posean la misma caracteristica especificada.
    def filter_by_mark(
        self, 
        marca: Marca,
        
    ) -> List[Auto]:
        return Auto.objects.filter(mark=marca)

    # Filtrar los productos que posean la misma caracteristica especificada.
    def filter_by_anio(
        self, 
        anio: Anio,
        
    ) -> List[Auto]:
        return Auto.objects.filter(year=anio)

    # Filtrar los productos que posean la misma caracteristica especificada.
    def filter_by_fuel(
        self, 
        combustible: Combustible,
        
    ) -> List[Auto]:
        return Auto.objects.filter(fuel=combustible)

    # Filtrar los productos que posean la misma caracteristica especificada.
    def filter_by_country(
        self, 
        pais: Pais,
        
    ) -> List[Auto]:
        return Auto.objects.filter(country=pais)

    # Elimiar un elemento específico de la lista.
    def delete(self, auto: Auto):
        return auto.delete()

    # Modifico un elemento de la lista.
    def update(
        self,
        auto: Auto,
        nombre: str,
        marca: Marca,
        precio: float,
        anio: Anio,
        combustible: Combustible,
        pais: Pais,

    ) -> Auto:

        # Reemplazo las caracteristicas anteriores del producto por las nuevas realizadas.
        auto.name = nombre
        auto.mark = marca
        auto.price = precio
        auto.year = anio
        auto.fuel = combustible
        auto.country = pais

        # Guardo las actualizaciones realizadas para que se mantengan una vez se cierre la página.
        auto.save()