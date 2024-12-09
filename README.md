# 🎬 Sistema de Gestión de Videoclub

Este proyecto es un sistema de gestión para un videoclub, que permite gestionar películas, socios y alquileres.

## 🌟 Características

- Gestión de películas: agregar, editar, eliminar y listar películas.
- Gestión de socios: agregar, editar, eliminar y listar socios.
- Gestión de alquileres: registrar, editar, eliminar y listar alquileres.
- Búsqueda de socios y visualización de su última película alquilada.

## 🛠️ Requisitos

- Python 3.x
- Tkinter (incluido en Python)
- SQLite (incluido en Python)

## 📦 Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```

2. Navega al directorio del proyecto:
    ```sh
    cd tu-repositorio
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## 💻 Uso

1. Ejecuta el archivo principal del proyecto:
    ```sh
    python main.py
    ```

2. Utiliza la barra de menú superior para navegar entre las diferentes secciones del sistema:
    - Inicio
    - Películas
    - Socios
    - Alquileres

## 📂 Estructura del Proyecto

- `main.py`: Archivo principal para ejecutar la aplicación.
- `modelo/`: Contiene los archivos relacionados con la lógica de negocio y la base de datos.
  - `conexion_db.py`: Manejo de la conexión a la base de datos.
  - `pelicula_dao.py`: Operaciones CRUD para películas, socios y alquileres.
- `vista/`: Contiene los archivos relacionados con la interfaz gráfica de usuario.
  - `frame_inicio.py`: Frame de inicio.
  - `frame_peliculas.py`: Frame para gestionar películas.
  - `frame_socios.py`: Frame para gestionar socios.
  - `frame_alquileres.py`: Frame para gestionar alquileres.
  - `barrita_menu.py`: Configuración de la barra de menú.

## 🗃️ Base de Datos

El proyecto utiliza SQLite para almacenar la información de películas, socios y alquileres. Las tablas se crean automáticamente si no existen.

- `peliculas`: Almacena información sobre las películas.
- `socios`: Almacena información sobre los socios.
- `alquileres`: Almacena información sobre los alquileres.

