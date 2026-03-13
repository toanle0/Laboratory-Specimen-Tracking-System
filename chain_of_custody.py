import sqlite3
from datetime import datetime

DB = "database/specimens.db"

def log_transfer(specimen_id, department, technician):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO chain_of_custody (specimen_id, department, technician, timestamp)
    VALUES (?, ?, ?, ?)
    """, (specimen_id, department, technician, timestamp))

    conn.commit()
    conn.close()

def view_chain(specimen_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT department, technician, timestamp
    FROM chain_of_custody
    WHERE specimen_id=?
    """, (specimen_id,))

    records = cursor.fetchall()
    conn.close()

    return records
