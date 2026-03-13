import sqlite3
from datetime import datetime

DB = "database/specimens.db"

def add_specimen(specimen_id, patient_id, sample_type):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    received_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO specimens VALUES (?, ?, ?, ?, ?)
    """, (specimen_id, patient_id, sample_type, received_time, "Received"))

    conn.commit()
    conn.close()

def update_status(specimen_id, status):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE specimens
    SET status=?
    WHERE specimen_id=?
    """, (status, specimen_id))

    conn.commit()
    conn.close()

def lookup_specimen(specimen_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM specimens WHERE specimen_id=?", (specimen_id,))
    result = cursor.fetchone()

    conn.close()
    return result
