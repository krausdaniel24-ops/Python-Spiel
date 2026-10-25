
import bcrypt
from database import conn, cursor




# Passwort zu Hash 
def hash_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()


# User-Regestrierung
def register_user(username, password_hash):
    cursor.execute("INSERT INTO Benutzer (BenutzerName, PasswortHash) VALUES (?, ?)", (username, password_hash))
    conn.commit()


def register_new(username, password):
    if len(username) < 10:
        return "Der Name muss mindestens 10 Zeichen haben."
    if len(password) < 15:
        return "Das Passwort muss mindestens 15 Zeichen haben."
    
    cursor.execute("SELECT * FROM Benutzer WHERE BenutzerName = ?", (username,))
    if cursor.fetchone() is not None:
        return "Der Name ist schon vergeben"
    
    password_hash = hash_password(password)
    register_user(username, password_hash)
    return "ok"



def login(username, password):
    cursor.execute("SELECT PasswortHash FROM Benutzer WHERE BenutzerName = ?", (username,))
    row = cursor.fetchone()
    if row is not None and bcrypt.checkpw(password.encode(), row[0].encode()):
        return True
    else:
        return False








