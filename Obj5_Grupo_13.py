# Mateo Dawidiuk, Legajo: 114814
from tkinter import *
from tkinter import messagebox

def obtener_usuarios_claves(usuario, clave, registro_users):
    if usuario in registro_users:
        if registro_users[usuario] == clave:
            messagebox.showinfo("", "Usuario y clave correctos")
        else:
            messagebox.showerror("", "Alguno de los datos es incorrecto")
    else:
        messagebox.showerror("", "Alguno de los datos es incorrecto")
    return

def registrar_usuario(usuario, clave, registro_users, ventana_registro):
    if usuario in registro_users:
        messagebox.showerror("", "Usuario ya existente")
    elif not usuario or not clave:
        messagebox.showerror("", "Usuario y clave son obligatorios")
    else:
        registro_users[usuario] = clave
        messagebox.showinfo("", "Nuevo usuario registrado")
        ventana_registro.destroy()
    return

def abrir_ventana_registro(registro_users):
    ventana_registro = Toplevel()
    ventana_registro.title("Registrar nuevo usuario")
    ventana_registro.iconbitmap("IMG_grupo_13.ico")
    ventana_registro.geometry("280x150")
    ventana_registro.resizable(0, 0)
    ventana_registro.config(bg="pink")

    nuevo_usuario = Label(ventana_registro, text="Nuevo Usuario:", bg="pink")
    nuevo_usuario.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    nueva_clave = Label(ventana_registro, text="Nueva Clave:", bg="pink")
    nueva_clave.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_nuevo_usuario = Entry(ventana_registro)
    entry_nuevo_usuario.grid(row=0, column=1, padx=5, pady=5)
    entry_nueva_clave = Entry(ventana_registro, show="*")
    entry_nueva_clave.grid(row=1, column=1, padx=5, pady=5)
    boton_guardar = Button(ventana_registro, text="Guardar", command=lambda: registrar_usuario(entry_nuevo_usuario.get(), entry_nueva_clave.get(), registro_users, ventana_registro), cursor="hand2")
    boton_guardar.grid(row=2, column=1, sticky="w", padx=5, pady=10)

    return

def main():
    registro_users = {
            "Mateo Dawidiuk": "123",
            "Tahiel Devoto": "456",
            "Patricio Olesen": "789",
            "Ignacio Sigal": "000",
            "Joaquin Tapia": "Messi"
        }
    
    raiz = Tk()

    raiz.title("Login grupo 13")
    raiz.iconbitmap("IMG_grupo_13.ico")
    raiz.geometry("300x130")
    raiz.resizable(0,0)
    raiz.config(bg="pink")

    usuario = Label(raiz, text="Usuario alumno:", bg="pink")
    usuario.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    clave = Label(raiz, text="Clave:", bg="pink")
    clave.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_usuario = Entry(raiz)
    entry_usuario.grid(row=0, column=1, padx=5, pady=5)
    entry_clave = Entry(raiz, show="*")
    entry_clave.grid(row=1, column=1, padx=5, pady=5)
    boton_enviar = Button(raiz, text="Enviar", command=lambda: obtener_usuarios_claves(entry_usuario.get(), entry_clave.get(), registro_users), cursor="hand2")
    boton_enviar.grid(row=3, column=1, sticky="w", padx=8, pady=5)
    boton_registrar = Button(raiz, text="Registrar", command=lambda: abrir_ventana_registro(registro_users), cursor="hand2")
    boton_registrar.grid(row=4, column=1, sticky="w", padx=8, pady=2)

    raiz.mainloop()

main()
