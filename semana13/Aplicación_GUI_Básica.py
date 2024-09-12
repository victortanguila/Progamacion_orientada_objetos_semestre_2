import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Función para agregar información a la tabla
def agregar_informacion():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    if nombre and edad:
        try:
            edad = int(edad)
            tabla.insert("", tk.END, values=(nombre, edad))
            entrada_nombre.delete(0, tk.END)  # Limpiar el campo de nombre
            entrada_edad.delete(0, tk.END)  # Limpiar el campo de edad
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce un nombre y una edad.")

# Función para limpiar la tabla
def limpiar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)

# Crear la ventana principal
ventana = tk.Tk()

# Título descriptivo de la ventana principal
ventana.title("Sistema de Gestión de Datos de Usuarios")

# Tamaño de la ventana
ventana.geometry("800x400")

# Etiqueta para el nombre
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.pack(pady=5)

# Campo de entrada para el nombre
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# Etiqueta para la edad
etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_edad.pack(pady=5)

# Campo de entrada para la edad
entrada_edad = tk.Entry(ventana, width=30)
entrada_edad.pack(pady=5)

# Botón para agregar información
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_informacion)
boton_agregar.pack(pady=10)

# Tabla para mostrar la información agregada
tabla = ttk.Treeview(ventana, columns=("Nombre", "Edad"), show="headings", height=8)
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")

# Configurar la alineación de las columnas
tabla.column("Nombre", anchor=tk.CENTER, width=200)
tabla.column("Edad", anchor=tk.CENTER, width=100)

tabla.pack(pady=10)

# Botón para limpiar la tabla
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_tabla)
boton_limpiar.pack(pady=5)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
