import sqlite3

conn = sqlite3.connect("database/specimens.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS specimens (
    specimen_id TEXT PRIMARY KEY,
    patient_id TEXT,
    sample_type TEXT,
    received_time TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chain_of_custody (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    specimen_id TEXT,
    department TEXT,
    technician TEXT,
    timestamp TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id TEXT PRIMARY KEY,
    patient_name TEXT,
    dob TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized.")
