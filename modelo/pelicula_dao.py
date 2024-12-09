from .conexion_db import ConexionDB
from tkinter import messagebox
from datetime import datetime, timedelta

def verificar_y_crear_tablas():
    """
    Verifica si las tablas necesarias existen y las crea si no están presentes.
    """
    conexion = ConexionDB()

    tablas = {
        "peliculas": '''
        CREATE TABLE peliculas(
            id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100),
            duracion VARCHAR(10),
            genero VARCHAR(100),
            cantidad INTEGER
        )''',
        "socios": '''
        CREATE TABLE socios(
            id_socio INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100),
            apellido VARCHAR(100),
            telefono VARCHAR(20)
        )''',
        "alquileres": '''
        CREATE TABLE alquileres(
            id_alquiler INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pelicula INTEGER,
            id_socio INTEGER,
            fecha_salida DATE,
            fecha_entrega DATE,
            FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
            FOREIGN KEY(id_socio) REFERENCES socios(id_socio)
        )'''
    }

    try:
        for tabla, sql in tablas.items():
            conexion.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tabla}'")
            if not conexion.cursor.fetchone():
                conexion.cursor.execute(sql)
                print(f"Tabla '{tabla}' creada con éxito.")
        conexion.cerrar()
    except Exception as e:
        titulo = "Error al verificar o crear tablas"
        mensaje = f"Ha ocurrido un error: {e}"
        messagebox.showerror(titulo, mensaje)

class Pelicula:
    def __init__(self, nombre, duracion, genero, cantidad):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.cantidad = cantidad

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}, {self.cantidad}]'
    
def guardar(pelicula):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero, cantidad)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}', '{pelicula.cantidad}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla peliculas no esta creada en la base de datos'
        messagebox.showinfo(titulo, mensaje)

def listar():
    conexion = ConexionDB()

    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)

    return lista_peliculas

def listar_peliculas_actualizada():
    """
    Obtiene la lista de películas desde la base de datos tal como están almacenadas.
    """
    conexion = ConexionDB()
    sql = "SELECT * FROM peliculas"

    try:
        conexion.cursor.execute(sql)
        peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
        return peliculas
    except Exception as e:
        print(f"Error al listar películas: {e}")
        return []

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas 
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}', cantidad = '{pelicula.cantidad}'
    WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se pudo editar el registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se ha seleccionado un registro'
        messagebox.showerror(titulo, mensaje)

class Socio:
    def __init__(self, nombre, apellido, telefono):
        self.id_socio = None
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f'Socio[{self.nombre}, {self.apellido}, {self.telefono}]'

def guardar_socio(socio):
    conexion = ConexionDB()

    sql = f"""INSERT INTO socios (nombre, apellido, telefono)
    VALUES('{socio.nombre}', '{socio.apellido}', '{socio.telefono}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla socios no está creada en la base de datos'
        messagebox.showinfo(titulo, mensaje)

def listar_socios():
    conexion = ConexionDB()

    lista_socios = []
    sql = 'SELECT * FROM socios'

    try:
        conexion.cursor.execute(sql)
        lista_socios = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla de socios en la base de datos'
        messagebox.showinfo(titulo, mensaje)

    return lista_socios

def editar_socio(socio, id_socio):
    conexion = ConexionDB()

    sql = f"""UPDATE socios
    SET nombre = '{socio.nombre}', apellido = '{socio.apellido}',
    telefono = '{socio.telefono}'
    WHERE id_socio = {id_socio}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se pudo editar el registro'
        messagebox.showerror(titulo, mensaje)

def eliminar_socio(id_socio):
    conexion = ConexionDB()
    sql = f'DELETE FROM socios WHERE id_socio = {id_socio}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se ha seleccionado un registro'
        messagebox.showerror(titulo, mensaje)

class Alquiler:
    def __init__(self, id_pelicula, id_socio, fecha_salida, fecha_entrega):
        self.id_alquiler = None
        self.id_pelicula = id_pelicula
        self.id_socio = id_socio
        self.fecha_salida = fecha_salida
        self.fecha_entrega = fecha_entrega

    def __str__(self):
        return f'Alquiler[{self.id_pelicula}, {self.id_socio}, {self.fecha_salida}, {self.fecha_entrega}]'

def guardar_alquiler(alquiler):
    conexion = ConexionDB()

    sql = f"""INSERT INTO alquileres (id_pelicula, id_socio, fecha_salida, fecha_entrega)
    VALUES({alquiler.id_pelicula}, {alquiler.id_socio}, '{alquiler.fecha_salida}', '{alquiler.fecha_entrega}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        # Restar uno al stock de la película
        actualizar_cantidad_pelicula(alquiler.id_pelicula, 'restar')
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla alquileres no está creada en la base de datos'
        messagebox.showinfo(titulo, mensaje)

def listar_alquileres():
    conexion = ConexionDB()

    lista_alquileres = []
    sql = 'SELECT * FROM alquileres'

    try:
        conexion.cursor.execute(sql)
        lista_alquileres = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla de alquileres en la base de datos'
        messagebox.showinfo(titulo, mensaje)

    return lista_alquileres

def editar_alquiler(id_alquiler, id_pelicula, id_socio):
    conexion = ConexionDB()

    sql = f"""UPDATE alquileres
    SET id_pelicula = {id_pelicula}, id_socio = {id_socio}
    WHERE id_alquiler = {id_alquiler}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        print("Alquiler actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el alquiler: {e}")
        raise

def existe_id_pelicula(id_pelicula):
    conexion = ConexionDB()
    sql = f"SELECT id_pelicula FROM peliculas WHERE id_pelicula = {id_pelicula}"
    conexion.cursor.execute(sql)
    resultado = conexion.cursor.fetchone()
    conexion.cerrar()
    return resultado is not None

def existe_id_socio(id_socio):
    conexion = ConexionDB()
    sql = f"SELECT id_socio FROM socios WHERE id_socio = {id_socio}"
    conexion.cursor.execute(sql)
    resultado = conexion.cursor.fetchone()
    conexion.cerrar()
    return resultado is not None

def eliminar_alquiler(id_alquiler):
    conexion = ConexionDB()

    # Obtener el ID de la película del alquiler antes de eliminar
    sql_select = f"SELECT id_pelicula FROM alquileres WHERE id_alquiler = {id_alquiler}"
    sql_delete = f"DELETE FROM alquileres WHERE id_alquiler = {id_alquiler}"

    try:
        conexion.cursor.execute(sql_select)
        id_pelicula = conexion.cursor.fetchone()[0]

        conexion.cursor.execute(sql_delete)
        conexion.cerrar()

        # Sumar uno al stock de la película
        actualizar_cantidad_pelicula(id_pelicula, 'sumar')
    except Exception as e:
        print(f"Error al eliminar el alquiler: {e}")

def actualizar_cantidad_pelicula(id_pelicula, operacion):
    """
    Actualiza la cantidad de la película según la operación ('restar' o 'sumar').
    """
    conexion = ConexionDB()
    if operacion == 'restar':
        sql = f"UPDATE peliculas SET cantidad = cantidad - 1 WHERE id_pelicula = {id_pelicula} AND cantidad > 0"
    elif operacion == 'sumar':
        sql = f"UPDATE peliculas SET cantidad = cantidad + 1 WHERE id_pelicula = {id_pelicula}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        print(f"Error al actualizar la cantidad de la película: {e}")

def listar_peliculas_actualizadas():
    """
    Lista las películas con la cantidad ajustada según los alquileres.
    """
    conexion = ConexionDB()
    sql = """
    SELECT p.id_pelicula, p.nombre, p.duracion, p.genero, 
           (p.cantidad - COALESCE(SUM(a.id_pelicula = p.id_pelicula), 0)) AS cantidad_disponible
    FROM peliculas p
    LEFT JOIN alquileres a ON p.id_pelicula = a.id_pelicula
    GROUP BY p.id_pelicula
    """

    try:
        conexion.cursor.execute(sql)
        peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
        return peliculas
    except Exception as e:
        print(f"Error al listar películas actualizadas: {e}")
        return []

def alquilar_pelicula(id_pelicula, id_socio):
    conexion = ConexionDB()

    # Verificar si la película tiene unidades disponibles
    sql_verificar = f"SELECT nombre, cantidad FROM peliculas WHERE id_pelicula = {id_pelicula}"
    conexion.cursor.execute(sql_verificar)
    pelicula = conexion.cursor.fetchone()

    if pelicula and pelicula[1] > 0:  # Si la película existe y tiene unidades disponibles
        nombre_pelicula = pelicula[0]

        # Registrar el alquiler
        fecha_salida = datetime.now().strftime('%Y-%m-%d')
        fecha_entrega = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')

        sql_alquiler = f"""
        INSERT INTO alquileres (id_pelicula, id_socio, fecha_salida, fecha_entrega)
        VALUES ({id_pelicula}, {id_socio}, '{fecha_salida}', '{fecha_entrega}')
        """
        conexion.cursor.execute(sql_alquiler)

        # Restar uno al stock de la película
        actualizar_cantidad_pelicula(id_pelicula, 'restar')
        conexion.cerrar()

        return {
            "status": "success",
            "mensaje": f"Alquiler registrado con éxito.",
            "datos": {
                "nombre_pelicula": nombre_pelicula,
                "id_socio": id_socio,
                "fecha_salida": fecha_salida,
                "fecha_entrega": fecha_entrega
            }
        }
    else:
        conexion.cerrar()
        return {
            "status": "error",
            "mensaje": "No quedan unidades disponibles de esta película."
        }

def buscar_cliente(id_socio):
    """
    Busca los datos del cliente y su última película alquilada.
    """
    conexion = ConexionDB()
    sql_cliente = f"SELECT * FROM socios WHERE id_socio = {id_socio}"
    sql_alquiler = f"""
    SELECT peliculas.nombre, alquileres.fecha_salida 
    FROM alquileres
    JOIN peliculas ON alquileres.id_pelicula = peliculas.id_pelicula
    WHERE alquileres.id_socio = {id_socio}
    ORDER BY alquileres.fecha_salida DESC
    LIMIT 1
    """

    try:
        conexion.cursor.execute(sql_cliente)
        cliente = conexion.cursor.fetchone()

        conexion.cursor.execute(sql_alquiler)
        ultima_pelicula = conexion.cursor.fetchone()

        conexion.cerrar()

        if cliente and ultima_pelicula:
            return {
                "cliente": {
                    "id_socio": cliente[0],
                    "nombre": cliente[1],
                    "apellido": cliente[2],
                    "telefono": cliente[3]
                },
                "ultima_pelicula": {
                    "nombre": ultima_pelicula[0],
                    "fecha_salida": ultima_pelicula[1]
                }
            }
        elif cliente:
            return {
                "cliente": {
                    "id_socio": cliente[0],
                    "nombre": cliente[1],
                    "apellido": cliente[2],
                    "telefono": cliente[3]
                },
                "ultima_pelicula": None
            }
        else:
            return None
    except Exception as e:
        print(f"Error al buscar cliente: {e}")
        return None
