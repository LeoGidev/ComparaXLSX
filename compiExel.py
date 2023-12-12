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
    global dato1
    dato1=""
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
    
    dato1 = hoja1[resultado]
    
    
    
    

def buscador2():
    global dato2
    dato2=""
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
ventana.geometry("500x500")
  
#el color del la ventana en blanco
ventana.config(background = "white")
ventana.columnconfigure(0, weight=0)
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(3, weight=1)




  
# se hace el lavel que donde se pondrá la ruta
cuadromensaje = Label(ventana, text = "Bienvenido", width = 10, height = 4, fg = "red")
cuadromensaje.grid(pady=10, padx=10,row=8,column=0,columnspan=3,sticky=S+N+E+W)

 #archivo 1 
Label(ventana, text="Ingrese el nombre de la columna del primer archivo").grid(row=0, column=0, pady=10, padx=10)

texto=Text(ventana, height=1, width=10)
texto.grid(row=0, column=1, sticky=W, pady=10, padx=10)

boton1 = Button(ventana,text = "Abrir",command = buscador1).grid(row = 0, column= 2,sticky=W, pady=10, padx=10)

#archivo 2
Label(ventana, text="Ingrese el nombre de la columna del segundo archivo:").grid(row=1, column=0, pady=10, padx=10)   
texto2=Text(ventana, height=1, width=10)
texto2.grid(row=1, column=1, sticky=W, pady=10, padx=10)
boton2 = Button(ventana,text = "Abrir",command = buscador2).grid(row = 1, column=2, sticky=W, pady=10, padx=10)


boton3 = Button(ventana, text = "comparar", command = comparar).grid(pady=10, padx=10,row=2,column=0,columnspan=3,sticky=S+N+E+W)
  
#botonsalir = Button(ventana, text = "Salir", command = exit).grid(pady=10, padx=10,row=6,column=0,columnspan=3,sticky=S+N+E+W)






  



  

ventana.mainloop()

