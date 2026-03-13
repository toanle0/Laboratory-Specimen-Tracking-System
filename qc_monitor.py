import sqlite3

DB = "database/specimens.db"

def check_missing_status():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT specimen_id
    FROM specimens
    WHERE status IS NULL OR status=''
    """)

    issues = cursor.fetchall()
    conn.close()

    return issues


def check_duplicate_ids():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT specimen_id, COUNT(*)
    FROM specimens
    GROUP BY specimen_id
    HAVING COUNT(*) > 1
    """)

    duplicates = cursor.fetchall()
    conn.close()

    return duplicates
