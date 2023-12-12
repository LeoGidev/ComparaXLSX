import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
from pandas import ExcelWriter
from tkinter import *
from tkinter import filedialog

#funcion que busca archivo
def buscador1():
    archivo = filedialog.askopenfilename(initialdir = "/",
                                          title = "Elija un archivo",
                                          filetypes = (("Hoja de Excel",
                                                        "*.xls*"),
                                                       ("all files",
                                                        "*.*")))
    # Cambiamos el texto
    cuadroruta.configure(text="Archivo abierto: "+archivo)
    #abrimos excel
    hoja1 = pd.read_excel(archivo)

def buscador2():
    archivo2 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Elija un archivo",
                                          filetypes = (("Hoja de Excel",
                                                        "*.xls*"),
                                                       ("all files",
                                                        "*.*")))    
    hoja2 = pd.read_excel(archivo2)
    # Cambiamos el texto
    cuadroruta2.configure(text="Archivo abierto: "+archivo2)


# se crea la ventana
ventana = Tk()
  
# el titulo de la ventana
ventana.title('Compi')
  
# el ancho de la ventana
ventana.geometry("800x500")
  
#el color del la ventana en blanco
ventana.config(background = "white")
  
# se hace ek lavel que donde se pondrá la ruta
cuadroruta = Label(ventana,
                            text = "Explorador usando tkinter",
                            width = 100, height = 4,
                            fg = "red")
  
      
boton1 = Button(ventana,text = "Abrir",command = buscador1)
  
botonsalir = Button(ventana, text = "Salir", command = exit)
# se hace ek lavel que donde se pondrá la ruta
cuadroruta2 = Label(ventana,
                            text = "Explorador usando tkinter",
                            width = 100, height = 4,
                            fg = "red")
  
      
boton2 = Button(ventana,text = "Abrir",command = buscador2)
  


#se ubican las cosas por medio de la grilla
cuadroruta.grid(column = 1, row = 1)
cuadroruta2.grid(column = 1, row = 2)
  
boton1.grid(column = 1, row = 3)
boton2.grid(column = 1, row = 4)
  
botonsalir.grid(column = 1,row = 5)
  

ventana.mainloop()

