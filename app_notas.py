import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('440x500')
ventana.resizable(False,False)
ventana_caja = tk.Text(ventana,height=3,font='arial 20')

def abrir_ventana_texto():
    ventana_caja.grid(column=0, row=2, columnspan=9999)
    ventana_caja.focus()

Boton_crear = ttk.Button(ventana, text='Crear nota', command=abrir_ventana_texto)
Boton_crear.grid(column=0, row=0, columnspan=9, padx=100)

def guardar_nota(nombre_archivo):
    contenido = ventana_caja.get(1.0,tk.END)
    ruta = os.path.join(os.getcwd(), 'notas', nombre_archivo)
    with open(ruta, 'w') as archivo:
        archivo.write(contenido)

def cargar_nota(nombre_archivo):
    ruta = os.path.join(os.getcwd(), 'notas', nombre_archivo)
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    return contenido

def ventana_guardados():
    ventana_notas_guardadas = tk.Tk()
    caja_texto_cargada = tk.Text(ventana_notas_guardadas,height=5,font='arial')
    caja_texto_cargada.grid(column=1, row=2)
    
    def cargar_contenido(nombre_archivo):
        contenido = cargar_nota(nombre_archivo)
        caja_texto_cargada.delete(1.0, tk.END)
        caja_texto_cargada.insert(tk.END, contenido)
    
    boton_lista_cargada1 = ttk.Button(ventana_notas_guardadas, text='Nota 1', command=lambda: cargar_contenido('nota1'))
    boton_lista_cargada1.grid(column=1, row=3)
    
    boton_lista_cargada2 = ttk.Button(ventana_notas_guardadas, text='Nota 2', command=lambda: cargar_contenido('nota2'))
    boton_lista_cargada2.grid(column=1, row=4)
    
    boton_lista_cargada3 = ttk.Button(ventana_notas_guardadas, text='Nota 3', command=lambda: cargar_contenido('nota3'))
    boton_lista_cargada3.grid(column=1, row=5)
    
    boton_lista_cargada4 = ttk.Button(ventana_notas_guardadas, text='Nota 4', command=lambda: cargar_contenido('nota4'))
    boton_lista_cargada4.grid(column=1, row=6)
    
    boton_lista_cargada5 = ttk.Button(ventana_notas_guardadas, text='Nota 5', command=lambda: cargar_contenido('nota5'))
    boton_lista_cargada5.grid(column=1, row=7)
    
    ventana_notas_guardadas.mainloop()



def messagebox1():
    messagebox.showinfo(
    title='Nota guardada',
    message='La nota 1 ha sigo guardada correctamente'
)
    
def messagebox2():
    messagebox.showinfo(
    title='Nota guardada',
    message='La nota 2 ha sigo guardada correctamente'
)
    
def messagebox3():
    messagebox.showinfo(
    title='Nota guardada',
    message='La nota 3 ha sigo guardada correctamente'
)
    
def messagebox4():
    messagebox.showinfo(
    title='Nota guardada',
    message='La nota 4 ha sigo guardada correctamente'
)
def messagebox5():
    messagebox.showinfo(
    title='Nota guardada',
    message='La nota 5 ha sigo guardada correctamente'
)
boton_guardar_nota1 = ttk.Button(ventana, text='Guardar nota 1', command=lambda: [guardar_nota('nota1'),messagebox1()], width=13)
boton_guardar_nota1.grid(column=0, row=4, columnspan=1, padx=0)

boton_guardar_nota2 = ttk.Button(ventana, text='Guardar nota 2', command=lambda: [guardar_nota('nota2'),messagebox2()], width=13)
boton_guardar_nota2.grid(column=1, row=4, columnspan=1, padx=0)

boton_guardar_nota3 = ttk.Button(ventana, text='Guardar nota 3', command=lambda: [guardar_nota('nota3'),messagebox3()], width=13)
boton_guardar_nota3.grid(column=2, row=4, columnspan=1, padx=0)

boton_guardar_nota4 = ttk.Button(ventana, text='Guardar nota 4', command=lambda: [guardar_nota('nota4'),messagebox4()], width=13)
boton_guardar_nota4.grid(column=3, row=4, columnspan=1, padx=0)        
boton_guardar_nota5 = ttk.Button(ventana, text='Guardar nota 5', command=lambda: [guardar_nota('nota5'),messagebox5()] ,width=13)
boton_guardar_nota5.grid(column=4, row=4, columnspan=1, padx=0)

boton_cargar = ttk.Button(ventana, text='Cargar nota', command=ventana_guardados)
boton_cargar.grid(column=0, row=5, columnspan=9)

ventana.mainloop()
# Hola