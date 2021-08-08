# Importamos sqlite3
import sqlite3
# Importamos las cajas de mensajes de tkinter
from tkinter import messagebox


class Todo:

    def __init__(self, window):
        # Establecemos la Conexión a la base de datos
        try:
            self.conn = sqlite3.connect('todos.db')
        except:
            # En caso de que ocurra un error mostramos un mensaje
            messagebox.showerror(
                'Error', 'Conexión fallida a la base de datos')
            window.quit()
        # Instaciamos el metodo cursor para ejecutar las solicitudes de la base de datos
        self.bd = self.conn.cursor()

    # Obtiene todas las tareas de la base de datos
    def getTodos(self):
        try:
            self.bd.execute('SELECT * FROM todos ORDER BY id DESC')
            return self.bd.fetchall()
        except sqlite3.OperationalError:
            self.bd.execute(
                'CREATE TABLE "todos" ("id"	INTEGER NOT NULL UNIQUE,"task"	TEXT NOT NULL,"completed"	INTEGER NOT NULL,"date"	TEXT,PRIMARY KEY("id" AUTOINCREMENT))')
            self.conn.commit()
            self.getTodos()
        except:
            messagebox.showerror(
                'Error', 'Ha Ocurrido un error al intentar obtener las tarea')

    # Añade una nueva tarea a la base de datos
    def addTodo(self, todo):
        try:
            self.bd.execute(
                'INSERT INTO todos (task,completed,date) VALUES (?,?,?)', todo)
            self.conn.commit()
        except:
            messagebox.showerror(
                'Error', 'Ha Ocurrido un error al intentar agregar una nueva tarea')

    # eliminar una tarea dependiendo al id que se le pase
    def deleteTodo(self, id):
        try:
            self.bd.execute('DELETE FROM todos WHERE id = ?', id)
            self.conn.commit()
        except:
            messagebox.showerror(
                'Error', 'Ha ocurrido un error al intentar eliminar una tarea')
                
    # Actualiza una tarea dependiendo al id que se le pase
    def updateTodo(self, newTask):
        try:
            self.bd.execute('UPDATE todos SET task = ? WHERE id = ?', newTask)
            self.conn.commit()
        except:
            messagebox.showerror(
                'Error', 'Ha ocurrido un error al intentar editar una tarea')

    # Cambia el estado de una tarea, a completado o pendiente
    def changeStatus(self,newStatu):
        try:
            self.bd.execute('UPDATE todos SET completed = ? WHERE id = ?', newStatu)
            self.conn.commit()
        except:
            messagebox.showerror(
                'Error', 'Ha ocurrido un error al intentar editar una tarea')
