from tkinter import Button, Entry, Label, LabelFrame
from tkinter.constants import E, EW, W


class UpdateViews:
    def __init__(self, window, todoId, updateTodo):
        self.wind = window
        self.wind.title('Actualizar Tarea')
        self.todoId = todoId
        self.updateTodo = updateTodo

        # Creamos un Label que tendra el titulo del programa
        Label(self.wind, text='Actualizar Tarea', font=('Arial', 12)).grid(
            row=0, column=0, columnspan=4, sticky=EW)

        # Creamos un Label para utilizarlo como separador
        Label(self.wind, text='').grid(row=1)

        # Creamos un Marco
        self.inputFrame = LabelFrame(self.wind, pady=10, padx=5)
        # Colocamos el Marco en la fila 1 y en la columna 0
        self.inputFrame.grid(row=2, column=0, columnspan=4)
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

        # Creamos un boton que llamara el controlador "self.updateTodo" para actualizar una tarea
        Button(self.wind, text='Actualizar Tarea', command=lambda: self.updateTodo(
            self.todoId, self.inputTask.get(), self.wind)).grid(row=4, column=0, columnspan=4, sticky=W + E)
