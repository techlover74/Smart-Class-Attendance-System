import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS attendance (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_name TEXT,
                        timestamp TEXT
                    )""")
    conn.commit()
    conn.close()

def log_attendance(student_name):
    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO attendance (student_name, timestamp) VALUES (?, ?)", (student_name, timestamp))
    conn.commit()
    conn.close()

