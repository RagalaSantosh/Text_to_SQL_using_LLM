import sqlite3
import random
import string

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()

table_info = """
CREATE TABLE IF NOT EXISTS Employee (
    EMPLOYEE_ID INTEGER PRIMARY KEY,
    NAME VARCHAR2(100),
    LEVEL VARCHAR2(100),
    SALARY NUMBER
);
"""
cursor.execute(table_info)

employees = [
    (1, "John Doe", "Junior", 50000),
    (2, "Jane Smith", "Mid", 65000),
    (3, "Alice Johnson", "Senior", 85000),
    (4, "Bob Brown", "Junior", 52000),
    (5, "Charlie Black", "Mid", 68000),
]


levels = ["Junior", "Mid", "Senior"]
salaries = range(50000, 120000, 5000)

def random_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank"]
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Black", "White", "Green", "Clark", "Davis", "Adams"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"


for i in range(6, 101):  
    name = random_name()
    level = random.choice(levels)
    salary = random.choice(salaries)
    employees.append((i, name, level, salary))


insert_query = "INSERT INTO Employee (EMPLOYEE_ID, NAME, LEVEL, SALARY) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_query, employees)


connection.commit()


connection.close()
