# Importamos el modulo de tkinter
from tkinter import *
#Importamos la Vista
from views.main_views import Main_Views

#En el caso de que este sea el archivo principal, la ventana
if __name__ == '__main__':
    #Inicializamos la ventana
    root = Tk()
    #Deshabilitamos la opcion de redimensionar la ventana
    root.resizable(False,False)
    #Incializamos la vista principal
    Main_Views(root)
    #Ejecutamos la ventana
    root.mainloop()
