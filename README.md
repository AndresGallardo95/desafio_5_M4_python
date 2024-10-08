# Gestión de Instancias de Usuario

## 1. Introducción
Este proyecto en Python permite la creación y gestión de instancias de usuarios a partir de un archivo de texto (`usuarios.txt`). Cada línea del archivo contiene datos en formato JSON que son utilizados para crear instancias de la clase `Usuario`. En caso de encontrar errores durante la lectura del archivo o la creación de instancias, el sistema registra los problemas en un archivo de log (`error.log`).

### Funcionalidades principales:
- Leer un archivo de texto con información de usuarios en formato JSON.
- Crear instancias de la clase `Usuario` con los datos proporcionados.
- Manejar y registrar errores en la lectura y procesamiento de datos.

Este proyecto es útil para demostrar el manejo de archivos, la creación de objetos desde datos externos y el tratamiento de excepciones en Python.

---

## 2. Instrucciones de Uso

### Requisitos:
- Python 3.x instalado en tu máquina.
- Un archivo `usuarios.txt` con datos en formato JSON de usuarios.
- El archivo `usuario.py` que contiene la definición de la clase `Usuario`.

### Pasos para ejecutar el programa:
1. **Clona el repositorio** o descarga los archivos en tu máquina local.
   
   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git
   cd tu-repositorio
