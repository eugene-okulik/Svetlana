import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

# 1st task: Create student
query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(query, ('Lana_Python', 'Night_Python'))
student_id = cursor.lastrowid

query = "SELECT * FROM students WHERE id = %s"
cursor.execute(query, (student_id,))
print(f"Student: {cursor.fetchone()}")

# 2nd task: Create books
query = f"INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"

cursor.executemany(
    query, [
        ('Python for beginners_2', student_id),
        ('Python for advanced_2', student_id),
        ('Python for professionals_2', student_id)
    ]
)

# 3rd task, part 1: Create group
query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(query, ('LanaNightPython group', '2024-07-01', '2024-11-01'))
group_id = cursor.lastrowid

# 3rd task, part 2: Add student to group
query = "UPDATE students s SET s.group_id = %s WHERE s.id = %s"
cursor.execute(query, (group_id, student_id))

# 4th task: Create subjects
query = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(
    query, [
        ('Science_2',),
        ('Math_2',),
        ('Python_2',)
    ]
)

subject_ids = [cursor.lastrowid + i for i in range(cursor.rowcount)]
print(subject_ids)

# 5th task: Create lessons
query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    query, [
        ('Introduction to Ethics_11', subject_ids[0]),
        ('Existentialism and Human Freedom_11', subject_ids[0]),
        ('Math for beginners_11', subject_ids[1]),
        ('Math for advanced_11', subject_ids[1]),
        ('Python for beginners_11', subject_ids[2]),
        ('Python for advanced_11', subject_ids[2])
    ]
)

lesson_ids = [cursor.lastrowid + i for i in range(cursor.rowcount)]
print(lesson_ids)

# 6th task: Create marks
query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    query, [
        (8, lesson_ids[0], student_id),
        (12, lesson_ids[1], student_id),
        (10, lesson_ids[2], student_id),
        (11, lesson_ids[3], student_id),
        (12, lesson_ids[4], student_id),
        (9, lesson_ids[5], student_id)
    ]
)

# 7th task: Get data for student
# 7.1: Get student's marks
query = f"""
SELECT s.name, s.second_name, m.value
FROM students s
join marks m
on s.id = m.student_id
WHERE s.id = {student_id}
"""
cursor.execute(query)
data = cursor.fetchall()

print('Marks:')
for item in data:
    print(item)

# 7.2: Get student's books
query = f"""
SELECT s.name, s.second_name, b.title
    FROM students s
    join books b
    on s.id = b.taken_by_student_id
    WHERE s.id = {student_id}
"""
cursor.execute(query)
data = cursor.fetchall()

print('Books:')
for item in data:
    print(item)

# 7.3.1: Get student's all data
query = f"""
SELECT
        g.title AS 'GROUP_NAME',
        s.id as 'STUDENT_ID',
        s.name as 'STUDENT_NAME',
        s.second_name as 'STUDENT_SECOND_NAME',
        b.title as 'BOOK_TITLE',
        sub.title as 'SUBJECT_TITLE',
        l.title as 'LESSON_TITLE',
        m.value as 'MARKS'
        FROM students s
        JOIN `groups` g ON s.group_id = g.id
        JOIN books b ON s.id = b.taken_by_student_id
        JOIN marks m ON s.id = m.student_id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjets sub ON sub.id = l.subject_id
        WHERE s.id = {student_id}   
"""

cursor.execute(query)
data = cursor.fetchall()

print("All data:")
for item in data:
    print(item)

# 7.3.2: Get student's all data
query = f"""
SELECT
g.title AS 'GROUP_NAME',
s.id as 'STUDENT_ID',
s.name as 'STUDENT_NAME',
s.second_name as 'STUDENT_SECOND_NAME',
sub.title as 'SUBJECT_TITLE',
l.title as 'LESSON_TITLE',
m.value as 'MARKS',
COUNT(b.id) as 'BOOK_COUNT'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON sub.id = l.subject_id
JOIN books b ON s.id = b.taken_by_student_id
WHERE s.id = {student_id}
GROUP BY
    s.id,
    g.title,
    s.name,
    s.second_name,
    m.value,
    sub.title,
    l.title
"""

cursor.execute(query)
data = cursor.fetchall()

print("All data 2:")
for item in data:
    print(item)

db.commit()
db.close()
