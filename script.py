import json
from usuario import Usuario

def leer_usuarios(archivo_usuarios):
    """
    Lee un archivo de texto con datos de usuarios en formato JSON y crea instancias de Usuario.
    
    Args:
    - archivo_usuarios (str): El nombre del archivo que contiene los datos de usuarios.
    
    Returns:
    - list: Una lista de instancias de la clase Usuario.
    
    Cualquier error al procesar una línea se registra en el archivo error.log.
    """
    usuarios = []  # Lista para almacenar las instancias de Usuario
    with open(archivo_usuarios, 'r') as file:
        for linea in file:
            try:
                # Convertir cada línea del archivo de texto en un diccionario usando json
                datos_usuario = json.loads(linea.strip())
                
                # Crear una instancia de Usuario usando los datos del diccionario
                usuario = Usuario(
                    nombre=datos_usuario.get('nombre'),
                    apellido=datos_usuario.get('apellido'),
                    email=datos_usuario.get('email'),
                    genero=datos_usuario.get('genero')
                )
                usuarios.append(usuario)  # Agregar el usuario a la lista
            except (json.JSONDecodeError, TypeError, KeyError) as e:
                # Manejo de excepciones y registro de errores
                with open('error.log', 'a') as error_file:
                    error_file.write(f"Error al procesar la línea: {linea.strip()} - {e}\n")
    return usuarios

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Llama a la función leer_usuarios para procesar el archivo 'usuarios.txt' 
    y luego imprime los usuarios creados.
    """
    lista_usuarios = leer_usuarios('usuarios.txt')  # Llamada a la función para leer los usuarios
    for usuario in lista_usuarios:
        print(usuario)  # Imprimir cada usuario creado
