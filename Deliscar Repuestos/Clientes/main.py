import sqlite3
import os

# Ruta al archivo de base de datos
db_path = os.path.join(os.path.dirname(__file__), 'database', 'database.db')

# Conectar a la base de datos (la crea si no existe)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Habilitar claves foráneas en SQLite
cursor.execute("PRAGMA foreign_keys = ON")

# Crear las tablas si no existen
cursor.execute('''
CREATE TABLE IF NOT EXISTS Persona (
    idPersona INTEGER PRIMARY KEY,
    idTelefono INTEGER,
    idMail INTEGER,
    Nombre TEXT NOT NULL,
    Apellido TEXT NOT NULL,
    Alias TEXT,
    FOREIGN KEY (idTelefono) REFERENCES Telefono(idTelefono),
    FOREIGN KEY (idMail) REFERENCES Mail(idMail)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Telefono (
    idTelefono INTEGER PRIMARY KEY,
    idPersona INTEGER,
    telefono TEXT NOT NULL,
    FOREIGN KEY (idPersona) REFERENCES Persona(idPersona)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Mail (
    idMail INTEGER PRIMARY KEY,
    idPersona INTEGER,
    mail TEXT NOT NULL,
    FOREIGN KEY (idPersona) REFERENCES Persona(idPersona)
);
''')

# Consultar las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tablas en la base de datos:", tables)

# Cerrar la conexión
conn.close()
