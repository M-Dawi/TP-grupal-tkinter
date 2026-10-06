# Mateo Dawidiuk, Legajo: 114814
from tkinter import *
from tkinter import messagebox

# Objetivo 1
def main():
    raiz = Tk()

    raiz.title("Login grupo 13")
    raiz.iconbitmap("IMG_grupo_13.ico")
    raiz.geometry("300x130")
    raiz.resizable(0,0)
    raiz.config(bg="pink")

    usuario = Label(raiz, text="Usuario alumno:", bg="pink")
    usuario.grid(row=0, column=0, sticky="e", padx=5, pady=8)
    clave = Label(raiz, text="Clave:", bg="pink")
    clave.grid(row=1, column=0, sticky="e", padx=5, pady=8)
    entry_usuario = Entry(raiz)
    entry_usuario.grid(row=0, column=1, padx=5, pady=8)
    entry_clave = Entry(raiz, show="*")
    entry_clave.grid(row=1, column=1, padx=5, pady=8)

    raiz.mainloop()

main()
