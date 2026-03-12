import sqlite3

#create connection
conn = sqlite3.connect("database.db")

# create cursor
cursor = conn.cursor()

#creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    name TEXT,
    marks INTEGER
)
""")
#clearing previous data if exists
cursor.execute("DELETE FROM student")


#insreting values
students = [
    ("Sahil", 95),
    ("Kaushik", 90),
    ("John", 89),
    ("Kara", 87),
    ("Simpson", 97)
]

cursor.executemany("Insert into student(name,marks) values (?,?)", students)
conn.commit()

print("Initial data:")

cursor.execute("SELECT * FROM student")
print(cursor.fetchall())

# a) Second topper in the class

cursor.execute("""
Select name,marks from student Order BY marks DESC limit 1 offset 1 """) 
print("Second Topper in class is:",cursor.fetchone())


# b) second topper in class if two students have same marks

# updating acoording to the second table
cursor.execute("UPDATE student SET marks = 97 WHERE name = 'Kaushik'")

print("After update for case b")
cursor.execute("SELECT * FROM student")
print(cursor.fetchall())

cursor.execute("""
SELECT name, marks
FROM student
ORDER BY marks DESC, name ASC
LIMIT 1 OFFSET 1
""")

print("Second topper is:", cursor.fetchone())


# c second topper when sahre same rank case) 

cursor.execute("""
UPDATE student
SET marks = 95
WHERE name = 'John'
""")


conn.commit()
print("Update for case c")
cursor.execute("SELECT * FROM student")
print(cursor.fetchall())


cursor.execute("""
SELECT name, marks
FROM (
    SELECT name, marks,
           DENSE_RANK() OVER (ORDER BY marks DESC) AS rnk
    FROM student
)
WHERE rnk = 2
""")

print("Second rank toppers:", cursor.fetchall())

conn.close()

 

