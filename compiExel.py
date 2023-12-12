import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
from pandas import ExcelWriter
from tkinter import *
from tkinter import filedialog

#funcion que busca archivo
def buscador():
    archivo = filedialog.askopenfilename(initialdir = "/",
                                          title = "Elija un archivo",
                                          filetypes = (("Hoja de Excel",
                                                        "*.xlsx*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Cambiamos el texto
    label_file_explorer.configure(text="Archivo abierto: "+archivo)


# se crea la ventana
ventana = Tk()
  
# el titulo de la ventana
ventana.title('Compi')
  
# el ancho de la ventana
ventana.geometry("800x500")
  
#el color del la ventana en blanco
ventana.config(background = "white")
  
# se hace ek lavel que donde se pondrá la ruta
label_file_explorer = Label(ventana,
                            text = "Explorador usando tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(ventana,text = "Abrir",command = buscador)
  
button_exit = Button(ventana, text = "Salir", command = exit)

#se ubican las cosas por medio de la grilla
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
  

ventana.mainloop()

