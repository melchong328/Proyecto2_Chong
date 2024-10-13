import os # Importamos modulo
from pelicula import Pelicula

class CatalogoPeliculas:
    def __init__(self, nombre_catalogo):
        # Atributos de clase
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"


# Método agregar(): Para agregar películas al archivo. 
    def agregar(self, pelicula):
        try: #  try-except para manejar errores.
            with open(self.ruta_archivo, 'a') as archivo:
                archivo.write(f'{pelicula.get_nombre()}\n')
            print(f"Película '{pelicula.get_nombre()}' agregada al catálogo.")
        except IOError:
            print(f"Error al agregar la película al catálogo '{self.nombre}'.")
        
# Método listar():  Para leer y mostrar las películas. 
    def listar(self):
        if not os.path.exists(self.ruta_archivo): 
            print(f"El catálogo '{self.nombre}' está vacío.")
            return
        
        try: #  try-except para manejar errores.
            with open(self.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines()
                if not peliculas:
                    print(f"'El catálogo '{self.nombre}' está vacío.")
                else:
                    print(f"Películas en el catálogo '{self.nombre}':")
                    for pelicula in peliculas:
                        print(f"- {pelicula.strip()}")
        except IOError:
            print(f"Error al leer el catálogo '{self.nombre}'.")

# Método eliminar(): Para borrar el archivo del catálogo.
    def eliminar(self):
        try: #  try-except para manejar errores.
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.nombre}' eliminado.")
        except FileNotFoundError:
            print(f"El catálogo '{self.nombre}' no existe.")
        except IOError:
            print(f"Error al eliminar el catálogo '{self.nombre}'.")

menu = '''
        CATÁLOGO DE PELÍCULAS
        ***** OPCIONES *****
    ============================

    [1] Agregar película
    [2] Listar películas
    [3] Eliminar catálogo
    [4] Salir

    ============================

        Selecciona una opción o presiona 'q' para salir
'''

print(menu)


