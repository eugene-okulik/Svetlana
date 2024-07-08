person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# Task 1
name, last_name, city, phone, country = person
print(f'Task 1:\n{name} {last_name} lives in {city}, {country}. You can call him by phone: {phone}')

# Task 2
res_1, res_2, res_3 = 'результат операции: 42', 'результат операции: 514', 'результат работы программы: 9'

index_1, index_2, index_3 = res_1.index(':') + 1, res_2.index(':') + 1, res_3.index(':') + 1

num_1, num_2, num_3 = (
    int(res_1[index_1:].strip()) + 10, int(res_2[index_2:].strip()) + 10, int(res_3[index_3:].strip()) + 10
)

print(f'Task 2:\n{num_1}, {num_2}, {num_3}')

# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Task 3:')
print('Students ' + ', '.join(students) + ' study these subjects: ' + ', '.join(subjects))
