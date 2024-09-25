# README

## Proyecto Notas en Flask

Este proyecto es una aplicación web para gestionar notas, desarrollada con Python y Flask. Utiliza un archivo de texto (`notes.txt`) para almacenar las notas, permitiendo a los usuarios crear, editar y eliminar notas de manera sencilla.

### Contenidos

- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Rutas](#rutas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

### Tecnologías utilizadas

- **Python**: Lenguaje de programación utilizado para el desarrollo de la aplicación.
- **Flask**: Framework web para Python.
- **HTML**: Lenguaje de marcado utilizado para la interfaz de usuario.

### Estructura del proyecto

/pyhton-taskNote  │ ├── /templates │ └── index.html # Vista principal de la aplicación │ ├── app.py # Archivo principal de la aplicación └── notes.txt # Archivo de texto para almacenar las notas

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Felo-Dev/pyhton-taskNote.git
   cd pyhton-taskNote

python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate

Uso

La aplicación estará disponible en http://127.0.0.1:5000/. Desde allí podrás agregar, editar y eliminar notas.
Rutas

    GET /: Renderiza la vista principal con todas las notas.
    POST /add_note: Agrega una nueva nota.
    POST /edit_note/<int:index>: Edita una nota existente en la posición especificada.
    GET /delete_note/<int:index>: Elimina una nota en la posición especificada.
