import tkinter as tk
from auth import login, register_new


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

    status = tk.Label(window, text="", bg="#442b2b", fg="white")
    status.pack()

    def login_klick():
        name = login_name.get()
        passwort = login_passwort.get()
        if login(name, passwort):
            status.config(text="Login erfolgreich!", fg="green")
            show_game()
        else:
            status.config(text="Name oder Passwort falsch", fg="red")

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

    status = tk.Label(window, text="", bg="#442b2b", fg="white")
    status.pack()


    def register_klick():
        name = reg_name.get()
        password = reg_passwort.get()
        result = register_new(name, password)
        if result == "ok":
            status.config(text="Registriert!", fg="green")
        else:
            status.config(text=result, fg="red")

    tk.Button(window, text="Registrieren", command=register_klick).pack()
    tk.Button(window, text="Zurück", command=show_login).pack()

def show_game():
    clear_window()
    tk.Label(window, text="Spiel startet!", font=("Impact 36"), fg="#89CFF0").pack()

show_login()
window.mainloop()