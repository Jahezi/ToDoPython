import sqlite3  # Import der SQLite-Bibliothek

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect("todorpg.db")

# Cursor erstellen
cursor = conn.cursor()

# Eine Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level INTEGER DEFAULT 1
)
""")


print("done")
# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
