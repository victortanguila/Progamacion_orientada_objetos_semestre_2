# una Aplicacion de Agenda Personal
import tkinter as tk
from tkinter import messagebox, ttk
import pickle

# Ruta del archivo donde se guardarán los eventos
ARCHIVO_EVENTOS = "eventos.pickle"

# Función para agregar un evento
def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")
        return
    # Insertar el nuevo evento en el TreeView
    tree.insert("", tk.END, values=(fecha, hora, descripcion))
    # Limpiar los campos de entrada
    entrada_fecha.delete(0, tk.END)
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)
    # Guardar los eventos en el archivo
    guardar_eventos()

# Función para eliminar el evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")
        return
    # Confirmar eliminación
    respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
    if respuesta:
        tree.delete(selected_item)
        # Guardar los eventos en el archivo
        guardar_eventos()

# Función para guardar los eventos en un archivo
def guardar_eventos():
    eventos = []
    for item in tree.get_children():
        eventos.append(tree.item(item, "values"))
    with open(ARCHIVO_EVENTOS, "wb") as archivo:
        pickle.dump(eventos, archivo)

# Función para cargar los eventos desde un archivo
def cargar_eventos():
    try:
        with open(ARCHIVO_EVENTOS, "rb") as archivo:
            eventos = pickle.load(archivo)
            for evento in eventos:
                tree.insert("", tk.END, values=evento)
    except FileNotFoundError:
        pass

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal Universitaria")
root.geometry("600x400")
root.configure(bg="#FFDAB9")  # Fondo color durazno

# Estilo para los componentes
estilo = ttk.Style()
estilo.configure("Treeview",
    font=("Arial", 10),
    background="#FFDAB9",
    fieldbackground="#FFDAB9"
)
estilo.configure("Treeview.Heading",
    font=("Arial", 12, "bold")
)
estilo.configure("Treeview.Cell",
    anchor='center',  # Centra el texto en las celdas
)

# Crear y organizar los frames
frame_lista = tk.Frame(root, bg="#FFDAB9")
frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

frame_entrada = tk.Frame(root, bg="#FFDAB9")
frame_entrada.pack(pady=10, padx=10, fill=tk.X)

frame_acciones = tk.Frame(root, bg="#FFDAB9")
frame_acciones.pack(pady=10, padx=10, fill=tk.X)

# Crear el TreeView para mostrar eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción del Evento")
tree.column("Fecha", anchor='center')  # Centra el texto en la columna
tree.column("Hora", anchor='center')      # Centra el texto en la columna
tree.column("Descripción", anchor='center')  # Centra el texto en la columna
tree.pack(fill=tk.BOTH, expand=True)

# Crear campos de entrada con etiquetas centradas
etiqueta_fecha = tk.Label(frame_entrada, text="Fecha (dd-mm-aaaa):", bg="#FFDAB9", fg="black", font=("Arial", 10, "bold"))
etiqueta_fecha.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entrada_fecha = tk.Entry(frame_entrada)
entrada_fecha.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)

etiqueta_hora = tk.Label(frame_entrada, text="Hora (HH:MM):", bg="#FFDAB9", fg="black", font=("Arial", 10, "bold"))
etiqueta_hora.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)

etiqueta_descripcion = tk.Label(frame_entrada, text="Descripción del Evento:", bg="#FFDAB9", fg="black", font=("Arial", 10, "bold"))
etiqueta_descripcion.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entrada_descripcion = tk.Entry(frame_entrada)
entrada_descripcion.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)

# Crear botones con estilo
boton_agregar = tk.Button(frame_acciones, text="Agregar Evento", command=agregar_evento, bg="green", fg="white", borderwidth=2, relief="solid")
boton_agregar.pack(side=tk.LEFT, padx=10)

boton_eliminar = tk.Button(frame_acciones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="green", fg="white", borderwidth=2, relief="solid")
boton_eliminar.pack(side=tk.LEFT, padx=10)

boton_salir = tk.Button(frame_acciones, text="Salir", command=root.quit, bg="red", fg="white", borderwidth=2, relief="solid")
boton_salir.pack(side=tk.RIGHT, padx=10)

# Cargar eventos al iniciar la aplicación
cargar_eventos()

# Ejecutar el bucle principal
root.mainloop()