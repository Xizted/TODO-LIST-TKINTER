#Importamos todo el modulo de tkinter
from tkinter import *
#Importamos el Widget TreeView
from tkinter.ttk import Treeview
#Importamos los controladores
from controllers.todosList import TodosList


class Main_Views:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Todo List App')
        # Creamos un Label que tendra el titulo del programa
        Label(self.wind, text='Todo List App', font=('Arial', 24)).grid(
            row=0, column=0, columnspan=4, sticky=EW)

        # Creamos un Label para utilizarlo como separador
        Label(self.wind, text='').grid(row=1)

        # Creamos un Marco
        self.inputFrame = LabelFrame(self.wind, pady=10, padx=5)
        # Colocamos el Marco en la fila 1 y en la columna 0
        self.inputFrame.grid(row=2, column=0,columnspan=4)
        # Creamos un label y lo posicionamos adentro del marco
        Label(self.inputFrame, text='Ingresa una nueva tarea').grid(
            row=0, column=0, pady=5, sticky=W)
        # Creamos un Entry
        self.inputTask = Entry(self.inputFrame, width=35)
        # Creamos un Entry y lo posicionamos en la fila 1 y en la columna 0
        self.inputTask.grid(row=1, column=0)
        self.inputTask.focus()
        # Creamos otro Label para utilizarlo como separador
        Label(self.wind, text='').grid(row=3)

        

       # Creamos un Treeview con 10 de altura y 2 columnas, el cual contendra las tareas
        self.todoList = Treeview(height=10, columns=2)
       # Lo Posicionamos en la fila 4, columna 0
        self.todoList.grid(row=4, column=0,columnspan=4)
        #Establecemos los nombre de las cabeceras
        self.todoList.heading('#0', text='Tareas', anchor=CENTER)
        self.todoList.heading('#1', text='Estado', anchor=CENTER)


        # Inicializamos el controlador
        self.todo_list = TodosList(self.wind,self.todoList)
        #Creamos un boton que llamara el controlador "newTodo" para agregar una nueva tarea
        Button(self.wind, text='Agregar Nueva Tarea', command=lambda: self.todo_list.newTodo(self.inputTask)).grid(row=5,column=0,sticky=W+E)
        #Creamos un boton que llamara el controlador "editTodo" para editar una tarea
        Button(self.wind, text='Editar Tarea', command=self.todo_list.openUpdateTodoWindow).grid(row=5,column=1,sticky=W+E,padx=5)
        #Creamos un boton que llamara el controlador "changeStatu" que cambiara el estado de la tarea
        Button(self.wind, text='Cambiar Estado', command=self.todo_list.setStatus).grid(row=5,column=2,sticky=W+E,padx=5)
        #Creamos un boton que llamara el controlador "deleteTodo" para eliminar una tarea
        Button(self.wind, text='Eliminar Tarea', command=self.todo_list.deleteTodo).grid(row=5,column=3,sticky=W+E)