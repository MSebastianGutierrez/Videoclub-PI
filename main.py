import tkinter as tk
from cliente.vista import Frame, FrameSocio, FrameAlquiler, FrameInicio, barrita_menu
from modelo.pelicula_dao import verificar_y_crear_tablas

def main():
    # Verificar y crear tablas automáticamente
    verificar_y_crear_tablas()
    
    ventana = tk.Tk()
    ventana.title('Videoclub')
    ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(False, False)

    # Crear un contenedor para los frames
    contenedor = tk.Frame(ventana)
    contenedor.pack(fill='both', expand=True)

    # Crear los frames para las diferentes secciones
    frame_inicio = FrameInicio(root=contenedor)
    frame_peliculas = Frame(root=contenedor)
    frame_socios = FrameSocio(root=contenedor)
    frame_alquileres = FrameAlquiler(root=contenedor)

    # Empaquetar únicamente el frame de inicio
    frame_inicio.pack(fill='both', expand=True)

    # Asegurarse de que los demás frames no se muestren al inicio
    frame_peliculas.pack_forget()
    frame_socios.pack_forget()
    frame_alquileres.pack_forget()

    # Configurar la barra de menú para navegación
    barrita_menu(ventana, frame_inicio, frame_peliculas, frame_socios, frame_alquileres)

    ventana.mainloop()

if __name__ == '__main__':
    main()
