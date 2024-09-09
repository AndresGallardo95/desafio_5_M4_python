# usuario.py

class Usuario:
    """
    Clase Usuario que representa a un usuario con atributos básicos.
    
    Atributos:
    - nombre: El nombre del usuario (str)
    - apellidos: El apellido del usuario (str)
    - email: El correo electrónico del usuario (str)
    - genero: El género del usuario (str)
    """
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        """
        Inicializa una instancia de la clase Usuario con los atributos nombre, apellido, email y genero.
        
        Args:
        - nombre (str): El nombre del usuario.
        - apellido (str): El apellido del usuario.
        - email (str): El correo electrónico del usuario.
        - genero (str): El género del usuario.
        """
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

    def __str__(self):
        """
        Devuelve una representación en cadena de un objeto Usuario.
        
        Returns:
        str: Una cadena con el nombre, apellidos, correo y género del usuario.
        """
        return f"{self.nombre} {self.apellidos} ({self.email}) - Género: {self.genero}"
