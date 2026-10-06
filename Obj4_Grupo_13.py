# Mateo Dawidiuk, Legajo: 114814
from tkinter import *
from tkinter import messagebox

def obtener_usuarios_claves(usuario, clave):
    registro_users = {
        "Mateo Dawidiuk": "123",
        "Tahiel Devoto": "456",
        "Patricio Olesen": "789",
        "Ignacio Sigal": "000",
        "Joaquin Tapia": "Messi"
    }

    if usuario in registro_users:
        if registro_users[usuario] == clave:
            messagebox.showinfo("", "Usuario y clave correctos")
        else:
            messagebox.showerror("", "Alguno de los datos es incorrecto")
    else:
        messagebox.showerror("", "Alguno de los datos es incorrecto")
    return


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
    boton_enviar = Button(raiz, text="Enviar", command=lambda: obtener_usuarios_claves(entry_usuario.get(), entry_clave.get()))
    boton_enviar.grid(row=3, column=1, sticky="w", padx=8, pady=10)

    raiz.mainloop()

main()
