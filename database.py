import sqlite3

conn = sqlite3.connect("spiel.db") # Verbindung zur Spiel-Datenbank
cursor = conn.cursor()