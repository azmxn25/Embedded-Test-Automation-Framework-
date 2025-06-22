import sqlite3
from config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS test_results (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 test_case TEXT,
                 accel_x INTEGER,
                 accel_y INTEGER,
                 accel_z INTEGER,
                 gyro_x INTEGER,
                 gyro_y INTEGER,
                 gyro_z INTEGER,
                 pass_fail TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def log_result(test_case, accel, gyro, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO test_results (test_case, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, pass_fail) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (test_case, accel[0], accel[1], accel[2], gyro[0], gyro[1], gyro[2], status))
    conn.commit()
    conn.close()
