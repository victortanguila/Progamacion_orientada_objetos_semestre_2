import tkinter as tk
from tkinter import messagebox

# Funciones para manejar eventos de la aplicación
def add_task(event=None):
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía")

def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        # Añadir un indicativo visual para la tarea completada (e.g., tachado)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, f"{task} (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Campo de entrada de tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Botones de acciones
frame_buttons = tk.Frame(root)
frame_buttons.pack()

btn_add_task = tk.Button(frame_buttons, text="Añadir Tarea", width=15, command=add_task)
btn_add_task.grid(row=0, column=0, padx=5)

btn_mark_completed = tk.Button(frame_buttons, text="Marcar como Completada", width=20, command=mark_completed)
btn_mark_completed.grid(row=0, column=1, padx=5)

btn_delete_task = tk.Button(frame_buttons, text="Eliminar Tarea", width=15, command=delete_task)
btn_delete_task.grid(row=0, column=2, padx=5)

# Lista de tareas (Listbox)
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Vincular la tecla Enter para añadir una tarea
root.bind('<Return>', add_task)

# Ejecutar la aplicación
root.mainloop()
