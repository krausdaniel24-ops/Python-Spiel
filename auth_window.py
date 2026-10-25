import tkinter as tk
from auth import login

window = tk.Tk()
window.title("Python-Game")
window.geometry("1000x850")
window.config(bg="#442b2b")


def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


def show_login():
    clear_window()
    tk.Label(window, text="Python-Game", font=("Impact", 36), fg="#445862").pack()

    tk.Label(window, text="Loginname:").pack()
    login_name = tk.Entry(window, bg="white", fg="black")
    login_name.pack()

    tk.Label(window, text="Passwort:").pack()
    login_passwort = tk.Entry(window, show="*", bg="white", fg="black")
    login_passwort.pack()

    def login_klick():
        name = login_name.get()
        passwort = login_passwort.get()
        if login(name, passwort):
            print("Login erfolgreich!")
        else:
            print("Name oder Passwort falsch.")

    tk.Button(window, text="Login", command=login_klick).pack()
    tk.Button(window, text="Registrieren", command=show_register).pack()


def show_register():
    clear_window()
    tk.Label(window, text="Python-Game", font=("Impact", 36), fg="#89CFF0").pack()
    tk.Label(window, text="Registrieren", font=("Impact", 25)).pack()

    tk.Label(window, text="Username:").pack()
    reg_name = tk.Entry(window, bg="white", fg="black")
    reg_name.pack()

    tk.Label(window, text="Password:").pack()
    reg_passwort = tk.Entry(window, show="*", bg="white", fg="black")
    reg_passwort.pack()

    tk.Button(window, text="Registrieren", font=("Impact", 15), fg="#272728").pack()
    tk.Button(window, text="Zurück", command=show_login).pack()


show_login()
window.mainloop()