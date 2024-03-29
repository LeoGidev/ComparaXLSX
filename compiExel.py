import pandas as pd
from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk
from ttkthemes import ThemedTk
from pandas import ExcelWriter
import os

class ComparadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Compi App')
        self.root.geometry("600x510")
        #self.root.config(background="white")
        self.root.set_theme('equilux')  
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))


        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
        self.create_result_frame()

    def create_labels_and_entries(self):
        Label(self.root, text="Ingrese el nombre de la columna del primer archivo:").grid(
            row=0, column=0, pady=10, padx=10)
        self.texto = Text(self.root, height=1, width=10)
        self.texto.grid(row=0, column=1, sticky='w', pady=10, padx=10)
        self.texto.bind('<KeyRelease>', self.check_entries)

        Label(self.root, text="Ingrese el nombre de la columna del segundo archivo:").grid(
            row=1, column=0, pady=10, padx=10)
        self.texto2 = Text(self.root, height=1, width=10)
        self.texto2.grid(row=1, column=1, sticky='w', pady=10, padx=10)
        self.texto2.bind('<KeyRelease>', self.check_entries)

    def create_buttons(self):
        self.btn1 = ttk.Button(self.root, text="Abrir", command=self.buscador1, state='disabled')
        self.btn1.grid(row=0, column=2, sticky='w', pady=10, padx=10)

        self.btn2 = ttk.Button(self.root, text="Abrir", command=self.buscador2, state='disabled')
        self.btn2.grid(row=1, column=2, sticky='w', pady=10, padx=10)

        ttk.Button(self.root, text="Comparar", command=self.comparar, state='disabled').grid(
            row=2, column=0, columnspan=3, pady=10, padx=10, sticky='snew')
        self.btn4=ttk.Button(self.root, text="Exportar", command=self.exportar, state="disabled")
        self.btn4.grid(row=4, column=0, columnspan=3, pady=10, padx=10, sticky='snew')
    def check_entries(self, event):
            # Verificar si ambos campos de entrada tienen contenido y habilitar los botones en consecuencia
            if self.texto.get("1.0", "end-1c") and self.texto2.get("1.0", "end-1c"):
                self.btn1['state'] = 'normal'
                self.btn2['state'] = 'normal'
                self.root.nametowidget(self.root.grid_slaves(row=2, column=0)[0]).config(state='normal')
                print("habilitar")
            else:
                print("desahbilitados")
                self.btn1['state'] = 'disabled'
                self.btn2['state'] = 'disabled'
                self.root.nametowidget(self.root.grid_slaves(row=2, column=0)[0]).config(state='disabled')

    def create_result_frame(self):
        self.ResultadoGeneral = ttk.LabelFrame(self.root, text="Resultados", padding=(20, 20))
        self.ResultadoGeneral.grid(row=3, column=0, columnspan=3, pady=10, padx=10, sticky='snew')

    def buscador1(self):
        try:
            archivo = filedialog.askopenfilename(initialdir="/",
                                                 title="Elija un archivo",
                                                 filetypes=(("Hoja de Excel", "*.xls*"),
                                                            ("all files", "*.*")))

            result = self.texto.get("1.0", "end")
            resultado = result.strip("\n")
            cuadromensaje = Label(self.ResultadoGeneral, text="Archivo abierto: " + archivo, background="#414141", foreground="white")
            cuadromensaje.pack()
            
            hoja1 = pd.read_excel(archivo)
            self.dato1 = hoja1[resultado]
        except Exception as e:
            cuadromensaje = Label(self.ResultadoGeneral, text="Error: " + str(e), background="#414141", foreground="white")
            cuadromensaje.pack()

    def buscador2(self):
        try:
            archivo2 = filedialog.askopenfilename(initialdir="/",
                                                  title="Elija un archivo",
                                                  filetypes=(("Hoja de Excel", "*.xls*"),
                                                             ("all files", "*.*")))
            result2 = self.texto2.get("1.0", "end")
            resultado2 = result2.strip('\n')
            cuadromensaje = Label(self.ResultadoGeneral, text="Archivo abierto: " + archivo2, background="#414141", foreground="white")
            cuadromensaje.pack()
            
            hoja2 = pd.read_excel(archivo2)
            self.dato2 = hoja2[resultado2]
        except Exception as e:
            cuadromensaje = Label(self.ResultadoGeneral, text="Error: " + str(e),background="#414141", foreground="white"
)
            cuadromensaje.pack()

    def comparar(self):
        coin = 0
        coinb = 0
        self.iguales = []
        self.soloA = []
        self.soloB = []

        cuadromensaje = Label(self.ResultadoGeneral, text="Listo!",background="#414141", foreground="white"
                              )
        cuadromensaje.pack()

        for n in list(self.dato1):
            for n2 in list(self.dato2):
                if n == n2:
                    self.iguales.append(n2)
                    coin = 1
            if coin == 0:
                self.soloA.append(n)
            else:
                coin = 0

        for nb in list(self.dato2):
            for nb2 in list(self.dato1):
                if nb == nb2:
                    coinb = 1
            if coinb == 0:
                self.soloB.append(nb)
            else:
                coinb = 0

        cuadromensaje_iguales = Label(self.ResultadoGeneral,
                                      text=f"Datos Repetidos {self.iguales}",
                                      background="#414141",
                                      foreground="white").pack()

        cuadromensaje_soloA = Label(self.ResultadoGeneral,
                                    text=f"Datos únicos en A {self.soloA}",
                                    background="#414141",
                                      foreground="white").pack()

        cuadromensaje_soloB = Label(self.ResultadoGeneral,
                                    text=f"Datos únicos en B {self.soloB}",
                                    background="#414141",
                                      foreground="white").pack()
        self.btn4['state'] = 'normal'
        
    
    

    def exportar(self):
        try:
            # Crear DataFrames para cada lista
            coincidentes = pd.DataFrame(self.iguales, columns=['Coincidencias'])
            soloA_df = pd.DataFrame(self.soloA, columns=['soloA'])
            soloB_df = pd.DataFrame(self.soloB, columns=['soloB'])
            
            # Unir los DataFrames en uno solo
            resultado_df = pd.concat([coincidentes, soloA_df, soloB_df], axis=1)
            
            # Ruta
            ruta_archivo = 'C:\\Users\\Work\\Desktop\\Resultado.xlsx'

            # Crear un objeto ExcelWriter
            with ExcelWriter(ruta_archivo, engine='openpyxl') as writer:
                # Guardar el DataFrame en una hoja llamada 'Resultado'
                resultado_df.to_excel(writer, sheet_name='Resultado', index=False)
            
            cuadromensaje = Label(self.ResultadoGeneral, text="Exportado Correctamente"+ ruta_archivo + "Click aquí para abrir", background="#414141",foreground="#C5FFE2")
            cuadromensaje.pack()
            cuadromensaje.bind("<Button-1>", self.abrir_carpeta)
        except:
            cuadromensaje = Label(self.ResultadoGeneral, text="Error al Exportar!", background="#414141",foreground="white")
            cuadromensaje.pack()

    def abrir_carpeta(self, event):
        carpeta_descargas = os.path.join(os.path.expanduser("~"), 'C:\\Users\\Work\\Desktop\\Resultado.xlsx')
        os.startfile(carpeta_descargas)

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = ComparadorApp(root)
    root.mainloop()
