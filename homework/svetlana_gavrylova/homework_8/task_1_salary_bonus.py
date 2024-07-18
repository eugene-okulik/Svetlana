import random

bonus_marker = [True, False]

while True:
    salary_input = input('Enter salary or type "exit" to finish: ')
    if salary_input == 'exit':
        break

    salary = int(salary_input)
    bonus = random.choice(bonus_marker)

    if bonus:
        total_salary = salary + random.randint(100, 300)
    else:
        total_salary = salary

    print(f'${salary}, {bonus} - ${total_salary}')
