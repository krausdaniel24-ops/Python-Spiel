import pygame 
import sqlite3 
import hashlib


Database = sqlite3.connect("spiel.db") # Verbindung zur Spiel-Datenbank
cursor = Database.cursor()



# User-Erstellung
def User():
    while True:
        User1 = input("Geben sie einen Benutzernamen ein: ")

        if len(User1) >= 10:
            print("Ihr Benutzername wurde erfolgreich gespeichert!")
            return User1
        else:
            print("Ihr Nutzername muss mindestens 10 Zeichen lang sein!")


# Passwort-Erstellung
def Password():
    while True:
        Password1 = input("Erstellen sie ein Passwort für ihren Account: ")

        if len(Password1) >= 15:
            print("Ihr Passwort wurde erfolgreich gespeichert!")
            return Password1
        else:
            print("Ihr Passwort muss mindestens 15 Zeichen enthalten!")



username = User()
password = Password()


cursor.execute("INSERT INTO Benutzer (BenutzerName, PasswortHash) VALUES (?, ?)", (username, "platzhalter"))
Database.commit()