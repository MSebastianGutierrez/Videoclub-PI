import tkinter as tk
from tkinter import ttk, messagebox
from modelo.pelicula_dao import Pelicula, guardar, listar, editar, eliminar, listar_peliculas_actualizada
from modelo.pelicula_dao import Socio, guardar_socio, listar_socios, editar_socio, eliminar_socio
from modelo.pelicula_dao import Alquiler, guardar_alquiler, listar_alquileres, editar_alquiler, eliminar_alquiler, buscar_cliente, existe_id_pelicula, existe_id_socio

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_pelicula = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.bloquear_campos()
        self.tabla_peliculas()

    def label_form(self):
        self.titulo = tk.Label(self, text="PELICULAS DE ESTRENO", font=('Arial', 16, 'bold'))
        self.titulo.grid(row=0, column=0, columnspan=3, pady=10)
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.label_duracion = tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=2, column=0, padx=10, pady=10)
        self.label_genero = tk.Label(self, text="Género: ")
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=3, column=0, padx=10, pady=10)
        self.label_cantidad = tk.Label(self, text="Cantidad: ")
        self.label_cantidad.config(font=('Arial', 12, 'bold'))
        self.label_cantidad.grid(row=4, column=0, padx=10, pady=10)

    def input_form(self):
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50)
        self.entry_duracion.grid(row=2, column=1, padx=10, pady=10)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50)
        self.entry_genero.grid(row=3, column=1, padx=10, pady=10)

        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self, textvariable=self.mi_cantidad)
        self.entry_cantidad.config(width=50)
        self.entry_cantidad.grid(row=4, column=1, padx=10, pady=10)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=5, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.btn_modi.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_modi.grid(row=5, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_cance.grid(row=5, column=2, padx=10, pady=10)

        # Botones
        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=7, column=0, padx=10, pady=10)

        self.btn_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.btn_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_eliminar.grid(row=7, column=1, padx=10, pady=10)

        self.btn_actualizar = tk.Button(self, text='Actualizar Tabla', command=self.actualizar_tabla_peliculas)
        self.btn_actualizar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_actualizar.grid(row=7, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        self.mi_cantidad.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_cantidad.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        self.mi_cantidad.set('')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_cantidad.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

    def guardar_datos(self):
        if not self.validar_datos_pelicula():
            return  # Si la validación falla, no guardar

        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
            int(self.mi_cantidad.get())
        )

        if self.id_pelicula is None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id_pelicula)

        self.tabla_peliculas()
        self.deshabilitar_campos()

    def validar_datos_pelicula(self):
        """
        Valida los datos ingresados en el formulario de películas.
        """
        nombre = self.mi_nombre.get().strip()
        duracion = self.mi_duracion.get().strip()
        genero = self.mi_genero.get().strip()
        cantidad = self.mi_cantidad.get().strip()

        # Validar que todos los campos estén llenos
        if not nombre or not duracion or not genero or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        
        # Validar que la duración sea un número
        if not duracion.isdigit():
            messagebox.showerror("Error", "La duración debe ser un número en minutos.")
            return False

        # Validar que el nombre y el género sean solo letras
        if not genero.isalpha() or not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre y el género deben contener solo letras.")
            return False

        # Validar que la cantidad sea un número positivo
        if not cantidad.isdigit():
            messagebox.showerror("Error", "La cantidad debe ser un número.")
            return False

        return True

    def tabla_peliculas(self):
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duracion', 'Genero', 'Cantidad'))
        self.tabla.grid(row=6, column=0, columnspan=6)

        # Crear un frame para contener la tabla y la barra de desplazamiento
        frame_tabla = tk.Frame(self)
        frame_tabla.grid(row=6, column=0, columnspan=4)

        # Crear la barra de desplazamiento
        scrollbar = ttk.Scrollbar(frame_tabla, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        # Crear la tabla
        self.tabla = ttk.Treeview(frame_tabla, columns=('ID Película', 'ID Socio', 'Fecha Salida', 'Fecha Entrega'), yscrollcommand=scrollbar.set)
        self.tabla.pack()

        # Configurar la barra de desplazamiento
        scrollbar.config(command=self.tabla.yview)


        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')
        self.tabla.heading('#4', text='CANTIDAD')

        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4]))

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]
            self.mi_cantidad_pelicula = self.tabla.item(self.tabla.selection())['values'][3]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
            self.entry_cantidad.insert(0, self.mi_cantidad_pelicula)

        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado un registro'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)

            self.tabla_peliculas()
            self.id_pelicula = None
        except:
            titulo = 'Eliminar registro'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

    def actualizar_tabla_peliculas(self):
        """
        Actualiza los datos de la tabla de películas desde la base de datos.
        """
        # Limpiar la tabla antes de recargar
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Recargar datos desde la base de datos con cantidades ajustadas
        lista_peliculas = listar_peliculas_actualizada()
        for pelicula in lista_peliculas:
            self.tabla.insert('', tk.END, text=pelicula[0], values=(pelicula[1], pelicula[2], pelicula[3], pelicula[4]))

        messagebox.showinfo("Actualización", "La tabla de películas se ha actualizado correctamente.")

class FrameInicio(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        # Etiquetas exclusivas para la bienvenida
        self.label_bienvenida = tk.Label(self, text="¡Bienvenido al Videoclub!", font=('Arial', 16, 'bold'))
        self.label_bienvenida.pack(pady=50)
        self.label_descripcion = tk.Label(self, text="Seleccione una opción en el menú superior para comenzar.", font=('Arial', 12))
        self.label_descripcion.pack(pady=10)

class FrameSocio(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_socio = None

        self.label_form_socio()
        self.input_form_socio()
        self.botones_principales_socio()
        self.bloquear_campos_socio()
        self.tabla_socios()

    def label_form_socio(self):
        self.titulo = tk.Label(self, text="SOCIOS", font=('Arial', 16, 'bold'))
        self.titulo.grid(row=0, column=0, columnspan=3, pady=10)
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=('Arial', 12, 'bold'))
        self.label_apellido.grid(row=2, column=0, padx=10, pady=10)
        self.label_telefono = tk.Label(self, text="Teléfono: ")
        self.label_telefono.config(font=('Arial', 12, 'bold'))
        self.label_telefono.grid(row=3, column=0, padx=10, pady=10)

    def input_form_socio(self):
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.mi_apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.mi_apellido)
        self.entry_apellido.config(width=50)
        self.entry_apellido.grid(row=2, column=1, padx=10, pady=10)

        self.mi_telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable=self.mi_telefono)
        self.entry_telefono.config(width=50)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)

    def botones_principales_socio(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos_socio)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=4, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_datos_socio)
        self.btn_modi.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_modi.grid(row=4, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos_socio)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_cance.grid(row=4, column=2, padx=10, pady=10)

    def habilitar_campos_socio(self):
        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_telefono.set('')

        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def deshabilitar_campos_socio(self):
        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_telefono.set('')

    def bloquear_campos_socio(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

    def guardar_datos_socio(self):
        if not self.validar_datos_socio():
            return  # Si la validación falla, no guardar

        socio = Socio(
            self.mi_nombre.get(),
            self.mi_apellido.get(),
            self.mi_telefono.get()
        )

        if self.id_socio is None:
            guardar_socio(socio)
        else:
            editar_socio(socio, self.id_socio)

        self.tabla_socios()
        self.deshabilitar_campos_socio()

    def validar_datos_socio(self):
        """
        Valida los datos ingresados en el formulario de socios.
        """
        nombre = self.mi_nombre.get().strip()
        apellido = self.mi_apellido.get().strip()
        telefono = self.mi_telefono.get().strip()

        # Validar que todos los campos estén llenos
        if not nombre or not apellido or not telefono:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False

        # Validar que el nombre y apellido sean solo letras
        if not nombre.isalpha() or not apellido.isalpha():
            messagebox.showerror("Error", "El nombre y el apellido deben contener solo letras.")
            return False

        # Validar que el teléfono sea solo números y tenga un máximo de 10 dígitos
        if not telefono.isdigit() or len(telefono) > 11:
            messagebox.showerror("Error", "El teléfono debe contener solo números y un máximo de 10 dígitos.")
            return False

        return True

    def tabla_socios(self):
        self.lista_socios = listar_socios()
        self.lista_socios.reverse()

        # Crear un frame para contener la tabla y la barra de desplazamiento
        frame_tabla = tk.Frame(self)
        frame_tabla.grid(row=5, column=0, columnspan=4)

        # Crear la barra de desplazamiento
        scrollbar = ttk.Scrollbar(frame_tabla, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        # Crear la tabla
        self.tabla = ttk.Treeview(frame_tabla, columns=('Nombre', 'Apellido', 'Teléfono'), yscrollcommand=scrollbar.set)
        self.tabla.pack()

        # Configurar la barra de desplazamiento
        scrollbar.config(command=self.tabla.yview)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='APELLIDO')
        self.tabla.heading('#3', text='TELÉFONO')

        for s in self.lista_socios:
            self.tabla.insert('', 0, text=s[0], values=(s[1], s[2], s[3]))

        # Botones
        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_datos_socio)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=6, column=0, padx=10, pady=10)

        self.btn_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos_socio)
        self.btn_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_eliminar.grid(row=6, column=1, padx=10, pady=10)

    def editar_datos_socio(self):
        try:
            self.id_socio = self.tabla.item(self.tabla.selection())['text']
            self.nombre_socio = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_socio = self.tabla.item(self.tabla.selection())['values'][1]
            self.telefono_socio = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos_socio()

            self.entry_nombre.insert(0, self.nombre_socio)
            self.entry_apellido.insert(0, self.apellido_socio)
            self.entry_telefono.insert(0, self.telefono_socio)

        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado un registro'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos_socio(self):
        try:
            self.id_socio = self.tabla.item(self.tabla.selection())['text']
            eliminar_socio(self.id_socio)

            self.tabla_socios()
            self.id_socio = None
        except:
            titulo = 'Eliminar registro'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

class FrameAlquiler(tk.Frame): 
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_alquiler = None

        self.label_form_alquiler()
        self.input_form_alquiler()
        self.botones_principales_alquiler()
        #self.bloquear_campos_alquiler()
        self.tabla_alquileres()

    def label_form_alquiler(self):
        self.titulo = tk.Label(self, text="ALQUILERES", font=('Arial', 16, 'bold'))
        self.titulo.grid(row=0, column=0, columnspan=3, pady=10)
        self.label_id_pelicula = tk.Label(self, text="ID Película: ")
        self.label_id_pelicula.config(font=('Arial', 12, 'bold'))
        self.label_id_pelicula.grid(row=1, column=0, padx=10, pady=10)
        self.label_id_socio = tk.Label(self, text="ID Socio: ")
        self.label_id_socio.config(font=('Arial', 12, 'bold'))
        self.label_id_socio.grid(row=2, column=0, padx=10, pady=10)

    def input_form_alquiler(self):
        self.mi_id_pelicula = tk.StringVar()
        self.entry_id_pelicula = tk.Entry(self, textvariable=self.mi_id_pelicula)
        self.entry_id_pelicula.config(width=50)
        self.entry_id_pelicula.grid(row=1, column=1, padx=10, pady=10)

        self.mi_id_socio = tk.StringVar()
        self.entry_id_socio = tk.Entry(self, textvariable=self.mi_id_socio)
        self.entry_id_socio.config(width=50)
        self.entry_id_socio.grid(row=2, column=1, padx=10, pady=10)

        self.entry_buscar_socio = tk.Entry(self)
        self.entry_buscar_socio.config(width=50)
        self.entry_buscar_socio.grid(row=3, column=1, padx=10, pady=10)

    def botones_principales_alquiler(self):
        self.btn_buscar = tk.Button(self, text='Buscar socio', command=self.buscar_y_mostrar_cliente)
        self.btn_buscar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1E1E1E', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_buscar.grid(row=3, column=0, padx=10, pady=10)

        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos_alquiler)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=4, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos_alquiler)
        self.btn_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos_alquiler)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_cance.grid(row=4, column=2, padx=10, pady=10)

        # Botones finales
        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_datos_alquiler)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=6, column=0, padx=10, pady=10)

        self.btn_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos_alquiler)
        self.btn_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_eliminar.grid(row=6, column=1, padx=10, pady=10) 

    def habilitar_campos_alquiler(self, modo_edicion=False):
        if not modo_edicion:  # Reiniciar solo si no es edición
            self.id_alquiler = None

        self.mi_id_pelicula.set('')
        self.mi_id_socio.set('')
        self.entry_id_pelicula.config(state='normal')
        self.entry_id_socio.config(state='normal')
        self.btn_guardar.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def deshabilitar_campos_alquiler(self):
        self.mi_id_pelicula.set('')
        self.mi_id_socio.set('')
        self.entry_id_pelicula.config(state='disabled')
        self.entry_id_socio.config(state='disabled')
        self.btn_guardar.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

    def guardar_datos_alquiler(self):
        try:
            # Validar campos obligatorios
            id_pelicula = self.mi_id_pelicula.get()
            id_socio = self.mi_id_socio.get()

            if not id_pelicula or not id_socio:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            # Validar que los IDs sean enteros
            id_pelicula = int(id_pelicula)
            id_socio = int(id_socio)

            # Verificar que la película y el socio existan
            if not existe_id_pelicula(id_pelicula):
                messagebox.showerror("Error", f"No se encontró una película con ID {id_pelicula}.")
                return

            if not existe_id_socio(id_socio):
                messagebox.showerror("Error", f"No se encontró un socio con ID {id_socio}.")
                return

            # Crear o editar el registro
            if self.id_alquiler is None:  # Nuevo alquiler
                from datetime import datetime, timedelta
                fecha_salida = datetime.now().strftime('%Y-%m-%d')
                fecha_entrega = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')

                alquiler = Alquiler(id_pelicula, id_socio, fecha_salida, fecha_entrega)
                guardar_alquiler(alquiler)
                messagebox.showinfo("Éxito", "Alquiler registrado correctamente.")
            else:  # Editar alquiler existente
                editar_alquiler(self.id_alquiler, id_pelicula, id_socio)
                messagebox.showinfo("Éxito", "Alquiler actualizado correctamente.")

            # Actualizar la tabla y limpiar el formulario
            self.tabla_alquileres()
            self.deshabilitar_campos_alquiler()

        except ValueError:
            messagebox.showerror("Error", "Los IDs deben ser números válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def editar_datos_alquiler(self):
        try:
            # Obtener el ID del alquiler seleccionado
            self.id_alquiler = self.tabla.item(self.tabla.selection())['text']
            id_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            id_socio = self.tabla.item(self.tabla.selection())['values'][1]

            # Habilitar campos y cargar valores
            self.habilitar_campos_alquiler(modo_edicion=True)
            self.mi_id_pelicula.set(id_pelicula)
            self.mi_id_socio.set(id_socio)

        except Exception as e:
            titulo = 'Edición de datos'
            mensaje = f'No ha seleccionado un registro o ocurrió un error: {e}'
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos_alquiler(self):
        try:
            # Obtener el ID del alquiler seleccionado
            self.id_alquiler = self.tabla.item(self.tabla.selection())['text']
            
            # Llamar a la función que elimina el alquiler en la base de datos
            eliminar_alquiler(self.id_alquiler)

            # Actualizar la tabla de alquileres
            self.tabla_alquileres()
            self.id_alquiler = None

        except Exception as e:
            titulo = 'Eliminar registro'
            mensaje = f'No ha seleccionado ningún registro o ocurrió un error: {e}'
            messagebox.showerror(titulo, mensaje)

    def tabla_alquileres(self):
        self.lista_alquileres = listar_alquileres()
        self.lista_alquileres.reverse()

        frame_tabla = tk.Frame(self)
        frame_tabla.grid(row=5, column=0, columnspan=4)

        scrollbar = ttk.Scrollbar(frame_tabla, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        self.tabla = ttk.Treeview(frame_tabla, columns=('ID Película', 'ID Socio', 'Fecha Salida', 'Fecha Entrega'), yscrollcommand=scrollbar.set)
        self.tabla.pack()
        scrollbar.config(command=self.tabla.yview)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='ID PELÍCULA')
        self.tabla.heading('#2', text='ID SOCIO')
        self.tabla.heading('#3', text='FECHA SALIDA')
        self.tabla.heading('#4', text='FECHA ENTREGA')

        for a in self.lista_alquileres:
            self.tabla.insert('', 0, text=a[0], values=(a[1], a[2], a[3], a[4]))   
  
    def buscar_y_mostrar_cliente(self):
        id_socio = self.entry_buscar_socio.get()
        if not id_socio.isdigit():
            messagebox.showerror("Error", "Por favor ingrese un ID válido.")
            return

        resultado = buscar_cliente(int(id_socio))

        if resultado:
            cliente = resultado["cliente"]
            ultima_pelicula = resultado["ultima_pelicula"]

            mensaje = f"Cliente: {cliente['nombre']} {cliente['apellido']}\nTeléfono: {cliente['telefono']}"
            if ultima_pelicula:
                mensaje += f"\nÚltima película alquilada: {ultima_pelicula['nombre']} (Salida: {ultima_pelicula['fecha_salida']})"
            else:
                mensaje += "\nEl cliente no tiene alquileres registrados."

            messagebox.showinfo("Resultado de búsqueda", mensaje)
        else:
            messagebox.showerror("Error", "No se encontró ningún cliente con ese ID.")

        # Borrar el contenido del campo de búsqueda
        self.entry_buscar_socio.delete(0, tk.END)

def mostrar_frame(frame_a_mostrar, *frames_a_ocultar):
    """
    Muestra el frame especificado y oculta los demás frames.
    """
    frame_a_mostrar.pack(fill='both', expand=True)
    for frame in frames_a_ocultar:
        frame.pack_forget()

def barrita_menu(ventana, frame_inicio, frame_peliculas, frame_socios, frame_alquileres):
    """
    Configura la barra de menú superior para la navegación entre frames.
    """
    menu = tk.Menu(ventana)
    
    # Menú "Inicio"
    menu.add_command(
        label="Inicio", 
        command=lambda: mostrar_frame(frame_inicio, frame_peliculas, frame_socios, frame_alquileres)
    )
    
    # Menú "Películas"
    menu.add_command(
        label="Películas", 
        command=lambda: mostrar_frame(frame_peliculas, frame_inicio, frame_socios, frame_alquileres)
    )
    
    # Menú "Socios"
    menu.add_command(
        label="Socios", 
        command=lambda: mostrar_frame(frame_socios, frame_inicio, frame_peliculas, frame_alquileres)
    )
    
    # Menú "Alquileres"
    menu.add_command(
        label="Alquileres", 
        command=lambda: mostrar_frame(frame_alquileres, frame_inicio, frame_peliculas, frame_socios)
    )
    
    # Menú "Salir"
    menu.add_command(label="Salir", command=ventana.quit)
    
    ventana.config(menu=menu)
