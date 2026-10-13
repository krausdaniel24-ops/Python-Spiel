import sqlite3

conn = sqlite3.connect("spiel.db") # Verbindung zur Spiel-Datenbank
cursor = conn.cursor()

# Verbindung zu Datenbank spiel.db + Öffnung und Auslesung der Inahlte der DB
def init_db():
    sql = open("Database.sql").read()
    cursor.executescript(sql)
    conn.commit()
