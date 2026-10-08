import pygame 
import sqlite3 
import hashlib
import os
import bcrypt

Database = sqlite3.connect("spiel.db") # Verbindung zur Spiel-Datenbank
cursor = Database.cursor()


# User-Erstellung
def User():
    while True:
        User1 = input("Geben sie einen Benutzernamen ein: ")

        if len(User1) >= 10:
            cursor.execute("SELECT * FROM Benutzer WHERE BenutzerName = ?", (User1,))
            row = cursor.fetchone()
            if row is None:
                print("Ihr Benutzername wurde erfolgreich gespeichert!")
                return User1
            else:
                print("Dieser Name ist schon vergeben, veruschen sie es erneut")
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


# Passwort zu Hash 
def hash_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()

password_hash = hash_password(password)


def register_user(username, password_hash):
    cursor.execute("INSERT INTO Benutzer (BenutzerName, PasswortHash) VALUES (?, ?)", (username, password_hash))
    Database.commit()

register_user(username, password_hash)