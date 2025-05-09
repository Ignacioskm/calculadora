import tkinter as tk
from tkinter import messagebox # Para Mensaje de error

#Ventana principal
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(0, 0)

#Colores que vamos a utilizar
color_texto = "#000000"
color_boton = "#e0e0e0"
color_boton_igual = "#4caf50"
color_boton_eliminar = "#072323"

#Crear pantalla de la calculadora
screen_text = tk.StringVar()
screen_label = tk.Label(root, textvariable=screen_text, font=("Arial",30), bg="#ffffff", fg=color_texto, anchor="e", padx=10)
screen_label.grid(row=0, column=0, columnspan=4, sticky="we", pady=10)

#Variable para manejar el contenido de la entrada
expression = ""

#Funciones para cuando apretemos los botones
def press(num):
    global expression
    expression += str(num)
    screen_text.set(expression)

def igualpress():
    try:
        global expression
        result = str(eval(expression))
        screen_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Entrada no valida")
        screen_text.set("")
        expression = ""

def clear():
    global expression
    screen_text.set("")
    expression= ""

#Definimos una lista con el contenido de los botones
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("+",4,2)
]

#Creamos un bucle for para que la libreria tome el contenido y cree los botones
for (text,row,col) in buttons:
    btn = tk.Button(root,text=text, width=5, height=2, font=("Arial",18), bg=color_boton, fg=color_texto, command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

#Le damos estilo a los botones distintos
igual_button = tk.Button(root,text="=", width=5, height=2, font=("Arial",18), bg=color_boton_igual, fg="#ffffff", command=igualpress)
igual_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

clear_button = tk.Button(root,text="c", width=5, height=2, font=("Arial",18), bg=color_boton_eliminar, fg="#ffffff", command=clear)
clear_button.grid(row=5, column=0,columnspan=4, padx=5, pady=5, sticky="nsew")

#Creamos un bucle para ajustar las filas y columnas para que ocupen el mismo espacio
for i in range(5):
    root.grid_rowconfigure(i,weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()