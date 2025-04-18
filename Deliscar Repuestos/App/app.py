import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import os

# Nombre del archivo de la base de datos
DATABASE = 'database.db'

def init_db():
    """Crea la base de datos y la tabla 'items' si no existen."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_items():
    """Obtiene todos los registros de la tabla 'items'."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return items

def add_item(name, description):
    """Agrega un nuevo registro a la tabla 'items'."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

def update_item(item_id, name, description):
    """Actualiza un registro existente."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name=?, description=? WHERE id=?", (name, description, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    """Elimina un registro de la tabla 'items'."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    conn.close()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD con Tkinter y SQLite")
        self.geometry("500x400")
        self.create_widgets()
        self.refresh_list()

    def create_widgets(self):
        # Listbox para mostrar los items
        self.listbox = tk.Listbox(self, width=60)
        self.listbox.pack(pady=10)

        # Frame para los botones
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        self.add_btn = tk.Button(btn_frame, text="Agregar", command=self.agregar)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        self.update_btn = tk.Button(btn_frame, text="Actualizar", command=self.actualizar)
        self.update_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar", command=self.eliminar)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

    def refresh_list(self):
        """Actualiza el contenido del Listbox con los registros actuales."""
        self.listbox.delete(0, tk.END)
        for item in get_items():
            # item es una tupla: (id, name, description)
            self.listbox.insert(tk.END, f"{item[0]} - {item[1]}: {item[2]}")

    def agregar(self):
        """Agrega un nuevo item pidiendo nombre y descripción."""
        name = simpledialog.askstring("Agregar", "Ingrese el nombre:")
        if name:
            description = simpledialog.askstring("Agregar", "Ingrese la descripción:")
            add_item(name, description)
            self.refresh_list()

    def actualizar(self):
        """Actualiza el item seleccionado."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un item para actualizar")
            return

        item_str = self.listbox.get(selected[0])
        item_id = int(item_str.split(" - ")[0])
        
        # Buscar el registro actual en la base de datos
        items = get_items()
        item_data = next((item for item in items if item[0] == item_id), None)
        if item_data:
            new_name = simpledialog.askstring("Actualizar", "Nuevo nombre:", initialvalue=item_data[1])
            new_desc = simpledialog.askstring("Actualizar", "Nueva descripción:", initialvalue=item_data[2])
            if new_name:
                update_item(item_id, new_name, new_desc)
                self.refresh_list()

    def eliminar(self):
        """Elimina el item seleccionado después de confirmar."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un item para eliminar")
            return

        item_str = self.listbox.get(selected[0])
        item_id = int(item_str.split(" - ")[0])
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este item?")
        if confirm:
            delete_item(item_id)
            self.refresh_list()

if __name__ == '__main__':
    # Inicializamos la base de datos solo si aún no existe
    if not os.path.exists(DATABASE):
        init_db()
    app = App()
    app.mainloop()
