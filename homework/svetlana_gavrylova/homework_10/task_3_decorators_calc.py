def proceed_calc(func):

    def wrapper(first, second):

        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            if second == 0:
                return 'Division by zero is not allowed'
            return func(first, second, '/')

    return wrapper


@proceed_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return round(first * second, 2)
    elif operation == '/':
        return round(first / second, 2)


num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))

print(calc(num_1, num_2))
