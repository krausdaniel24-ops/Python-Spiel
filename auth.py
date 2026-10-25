
import bcrypt
from database import conn, cursor


# User-Erstellung
def User():
    while True:
        User1 = input("Geben sie einen Benutzernamen ein: ")

        if len(User1) >= 10:
            cursor.execute("SELECT * FROM Benutzer WHERE BenutzerName = ?", (User1,))
            row = cursor.fetchone()
            if row is None:
                return User1
            else:
                print("Dieser Name ist schon vergeben, versuchen sie es erneut!")
        else:
            print("Ihr Nutzername muss mindestens 10 Zeichen lang sein!")


# Passwort-Erstellung
def Password():
    while True:
        Password1 = input("Erstellen sie ein Passwort für ihren Account: ")

        if len(Password1) >= 15:
            return Password1
        else:
            print("Ihr Passwort muss mindestens 15 Zeichen enthalten!")


# Passwort zu Hash 
def hash_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()


# User-Regestrierung
def register_user(username, password_hash):
    cursor.execute("INSERT INTO Benutzer (BenutzerName, PasswortHash) VALUES (?, ?)", (username, password_hash))
    conn.commit()


def register():
    username = User()
    password = Password()
    password_hash = hash_password(password)
    register_user(username, password_hash)
    print("Ihr Benutzer wurde erfolgreich gespeichert!")


def login(username, password):
    cursor.execute("SELECT PasswortHash FROM Benutzer WHERE BenutzerName = ?", (username,))
    row = cursor.fetchone()
    if row is not None and bcrypt.checkpw(password.encode(), row[0].encode()):
        return True
    else:
        return False


def login_klick():
    name = login_name.get()
    passwort = login_passwort.get()
    if login(name, passwort):
        print("Login erfolgreich!")
    else:
        print("Name oder Passwort falsch.")






