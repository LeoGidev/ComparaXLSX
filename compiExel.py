import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
from pandas import ExcelWriter
from tkinter import *
from tkinter import filedialog

dato1=''
dato2=''
iguales = []
soloA =[]
soloB =[]

#funcion que busca archivo
def buscador1():
    archivo = filedialog.askopenfilename(initialdir = "/",
                                          title = "Elija un archivo",
                                          filetypes = (("Hoja de Excel",
                                                        "*.xls*"),
                                                       ("all files",
                                                        "*.*")))
    #Se obtiene lo que diga el texto
    result=texto.get("1.0","end")
    resultado= result.strip("\n") #se borra la letra /n que se toma automaticamente al tomar el texto

    # Cambiamos el texto
    cuadromensaje.configure(text="Archivo abierto: "+archivo)
    #abrimos excel
    hoja1 = pd.read_excel(archivo)
    global dato1
    dato1 = hoja1[resultado]
    
    
    
    

def buscador2():
    archivo2 = filedialog.askopenfilename(initialdir = "/",
                                          title = "Elija un archivo",
                                          filetypes = (("Hoja de Excel",
                                                        "*.xls*"),
                                                       ("all files",
                                                        "*.*"))) 
    result2 = texto2.get("1.0","end")   
    resultado2 = result2.strip('\n')
    # Cambiamos el texto
    cuadromensaje.configure(text="Archivo abierto: "+archivo2)
    hoja2 = pd.read_excel(archivo2)
    global dato2
    dato2 = hoja2[resultado2]
    
    

#función que compara los dos bloques
def comparar():
    coin=0
    coinb=0
    
    
    for n in list(dato1):
       
        for n2 in list(dato2):
            print(n)
            print(n2)
            if n == n2:
                
                iguales.append(n2)
                coin=1
        if coin == 0:
            soloA.append(n)
        else: 
            coin = 0
    for nb in list(dato2):
        for nb2 in list(dato1):
            if nb == nb2:
                coinb=1
        if coinb == 0:
            soloB.append(nb)
        else:
            coinb = 0
    
    print("Iguales:")
    print(iguales)
    print("solo A: ", soloA)
    print("solo B: ", soloB)







# se crea la ventana
ventana = Tk()
  
# el titulo de la ventana
ventana.title('Compi')
  
# el ancho de la ventana
ventana.geometry("800x500")
  
#el color del la ventana en blanco
ventana.config(background = "white")
ventana.columnconfigure(0, weight=0)
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)

#texto del dato
texto=Text(ventana, height=1, width=10)
#texto del dato
texto2=Text(ventana, height=1, width=10)

  
# se hace ek lavel que donde se pondrá la ruta
cuadromensaje = Label(ventana,
                            text = "Bienvenido",
                            width = 100, height = 4,
                            fg = "red")
  
      
boton1 = Button(ventana,text = "Abrir",command = buscador1)
  
botonsalir = Button(ventana, text = "Salir", command = exit)

  
      
boton2 = Button(ventana,text = "Abrir",command = buscador2)

boton3 = Button(ventana, text = "comparar", command = comparar)
  


#se ubican las cosas por medio de la grilla


texto.grid(column=2,row=3)
texto2.grid(column=2,row=4)
  
boton1.grid(column = 1, row = 3)
boton2.grid(column = 1, row = 4)
boton3.grid(column=1, row= 5)
  
botonsalir.grid(column = 1,row = 6)

cuadromensaje.grid(pady=10,
                   padx=10,
                   row=8,
                   column=0,
                   columnspan=3,
                   sticky=S+N+E+W)
  

ventana.mainloop()

