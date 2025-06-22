import sqlite3

# Connect to the database
conn = sqlite3.connect("test_results.db")
cursor = conn.cursor()

# Fetch last 5 entries
cursor.execute("SELECT * FROM test_results ORDER BY timestamp DESC LIMIT 5")
rows = cursor.fetchall()

# Print the results
print("\n--- Last 5 Test Results ---\n")
for row in rows:
    print(f"ID: {row[0]}")
    print(f"Test Case: {row[1]}")
    print(f"Accel (X,Y,Z): {row[2]}, {row[3]}, {row[4]}")
    print(f"Gyro  (X,Y,Z): {row[5]}, {row[6]}, {row[7]}")
    print(f"Status: {row[8]}")
    print(f"Timestamp: {row[9]}")
    print("-" * 40)

conn.close()
