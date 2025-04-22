import sqlite3

# 1.
conn = sqlite3.connect("star_trek.db")
cursor = conn.cursor()

# 2. 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER )''')

data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

# 3.
cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?",
                ("Ezri Dax", "Jadzia Dax"))

# 4.
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()

print("Bajoran individuals:")
for name, age in results:
    print(f"{name} - {age} years old")

conn.commit()
conn.close()
