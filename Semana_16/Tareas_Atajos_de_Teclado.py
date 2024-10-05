import tkinter as tk
from tkinter import messagebox

class AplicacionGestionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada para nuevas tareas
        self.entry_task = tk.Entry(root, width=30)
        self.entry_task.pack(pady=10)

        # Botón para añadir tarea
        self.btn_add_task = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.btn_add_task.pack()

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=20)

        # Botones de completar y eliminar tareas
        self.btn_complete_task = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.btn_complete_task.pack(pady=5)
        self.btn_delete_task = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.btn_delete_task.pack(pady=5)

        # Atajos de teclado
        self.root.bind('<Return>', self.add_task_event)
        self.root.bind('<c>', self.complete_task_event)
        self.root.bind('<d>', self.delete_task_event)
        self.root.bind('<Delete>', self.delete_task_event)
        self.root.bind('<Escape>', lambda e: root.quit())

    def add_task(self):
        tarea = self.entry_task.get()
        if tarea:
            self.task_listbox.insert(tk.END, tarea)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Error de Entrada", "Por favor, introduce una tarea.")

    def add_task_event(self, event):
        self.add_task()

    def complete_task(self):
        indice_tarea_seleccionada = self.task_listbox.curselection()
        if indice_tarea_seleccionada:
            tarea = self.task_listbox.get(indice_tarea_seleccionada)
            # Marca visual de tarea completada (Ejemplo: tachar texto)
            self.task_listbox.delete(indice_tarea_seleccionada)
            self.task_listbox.insert(indice_tarea_seleccionada, f"[Completada] {tarea}")
        else:
            messagebox.showwarning("Error de Selección", "Por favor, selecciona una tarea para completar.")

    def complete_task_event(self, event):
        self.complete_task()

    def delete_task(self):
        indice_tarea_seleccionada = self.task_listbox.curselection()
        if indice_tarea_seleccionada:
            self.task_listbox.delete(indice_tarea_seleccionada)
        else:
            messagebox.showwarning("Error de Selección", "Por favor, selecciona una tarea para eliminar.")

    def delete_task_event(self, event):
        self.delete_task()

# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGestionTareas(root)
    root.mainloop()
