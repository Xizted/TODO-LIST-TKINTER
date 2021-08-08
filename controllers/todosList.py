from views.update_views import UpdateViews
from models.todo import Todo
from tkinter import Toplevel, messagebox
from tkinter import END
from datetime import datetime


class TodosList:
    def __init__(self, window, todoList):
        # Inizializamos el model
        self.model = Todo(window)
        # Almacenamos el TreeView de la vista para modificarlo
        self.todoList = todoList
        # Una vez inicializado el controlador, se obtendran todas las tareas
        self.getTodos()

    # Crea una nueva tarea y lo envia a la base de datos
    def newTodo(self, inputTask):
        task = inputTask.get()
        if self.verifiedInput(task):
            date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            todo = (task, 0, date)
            self.model.addTodo(todo)
            inputTask.delete(0, END)
        else:
            messagebox.showerror('Error', 'Por favor ingrese una tarea valida')
        self.getTodos()

    # Verificar si los inputs (entrie) estan vacios
    def verifiedInput(self,task):
        return task != ''

    # Obtienes todas las tareas desde la base de datos
    def getTodos(self):
        #En el caso de que se encuentre un registro en el treeview, se eliminaran todos
        register = self.todoList.get_children()
        for e in register:
            self.todoList.delete(e)

        # Comprobamos de si lo que devuelve la base de datos en de tipo 'NoneType',
        # En el caso de que sea verdadero, "todos" sera una lista vacia.
        # En el caso de ser falso, "todos" sera la lista de tarea que devuelve la base de datos
        todos = self.model.getTodos() if type(
            self.model.getTodos()) != 'NoneType' else []
        # Recorremos las tareas y la insertamos en el TreeView
        for todo in todos:
            self.todoList.insert(
                '', 0, id=todo[0], text=todo[1], values='Pendiente' if todo[2] == 0 else 'Completado')

    # Envia el id de la tarea a eliminar a la base de datos
    def deleteTodo(self):
        if self.notSelectedTodo():
            # Obtenemos el id de la tarea seleccionada
            id = (int(self.todoList.selection()[0]),)
            # lo enviamos al model para que ejecute la solicitud
            self.model.deleteTodo(id)
        else:
            messagebox.showerror(
                'Error', 'Por favor elige la tarea que desea eliminar')
        self.getTodos()

    # Envia el id y la nueva tarea a la base de datos para modificar un registro
    def updateTodo(self, id, task, updateWin):
        if self.verifiedInput(task):
            self.model.updateTodo((task, id))
            updateWin.destroy()
        else:
            messagebox.showerror('Error', 'Por favor ingrese una tarea valida')
        self.getTodos()


    # Abre la vista "update_views" en una nueva ventana
    def openUpdateTodoWindow(self):
        if self.notSelectedTodo():
            id = int(self.todoList.selection()[0])
            window = Toplevel()
            UpdateViews(window, id, self.updateTodo)
        else:
            messagebox.showerror(
                'Error', 'Por favor elige la tarea que desea editar')

    # Envia el id de la tarea a la base de datos para cambiar el estado de una tarea
    def setStatus(self):
        if self.notSelectedTodo():
            id = self.todoList.selection()[0]
            status = self.todoList.item(id)["values"][0]
            newStatus = 1 if status == 'Pendiente' else 0
            self.model.changeStatus((newStatus, int(id)))
        else:
            messagebox.showerror(
                'Error', 'Por favor elige la tarea que desea cambiar su estado')
        self.getTodos()

    # Verifica si el usuario selecciono una tarea
    def notSelectedTodo(self):
        value = self.todoList.selection()
        return len(value) != 0
