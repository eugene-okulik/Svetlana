import os
import csv
import collections
import dotenv

import mysql.connector as mysql

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

dotenv.load_dotenv()

students = collections.defaultdict(list)
with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    for row in file_data:
        key = (row['name'], row['second_name'])
        students[key].append(row)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)

for student, f_data in students.items():
    name, second_name = student

    query = """
    SELECT
        s.name as 'name',
        s.second_name as 'second_name',
        g.title AS 'group_title',
        b.title as 'book_title',
        sub.title as 'subject_title',
        l.title as 'lesson_title',
        m.value as 'mark_value'
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets sub ON sub.id = l.subject_id
    WHERE s.name = %s AND s.second_name = %s
    """

    cursor.execute(query, (name, second_name))
    data_from_db = cursor.fetchall()

    if data_from_db:
        for f_item in f_data:
            matched = False
            for db_item in data_from_db:
                if f_item == db_item:
                    matched = True
                    print(f'\nStudent {name} {second_name} exists, and the data matches the database:')
                    for key, value in f_item.items():
                        print(f'{key}: {value}')
                    break

            if not matched:
                print(f'\nStudent {name} {second_name} exists, but the data does not match in the database:')
                for key, value in f_item.items():
                    print(f'{key}: {value}')
    else:
        print(f'\nStudent {name} {second_name} is not found in the database.')

db.close()
