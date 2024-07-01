import random


# Function to perform operations with two numbers
def calculate_operations(a, b):
    sum_res = a + b
    sub_res = a - b
    multi_res = a * b

    return sum_res, sub_res, multi_res


# Function to generate two random numbers between 1 and 400
def generate_random_numbers(num_from=1, num_to=400):
    return random.randint(num_from, num_to), random.randint(num_from, num_to)


# Function to perform operations with two numbers input by the user
def input_numbers_manually():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        exit()

    return a, b


def get_numbers_from_user_choice():
    # Ask the user for their choice
    choice = input(
        "Do you want to use random numbers or enter numbers manually? (type 'random' or 'manual'): "
    ).strip().lower()

    choices = {
        'random': generate_random_numbers,
        'manual': input_numbers_manually
    }

    if choice not in choices:
        print("Invalid choice. Please type 'random' or 'manual'.")
        exit()

    return choices[choice]()


if __name__ == "__main__":
    # Get the numbers based on user choice
    num_1, num_2 = get_numbers_from_user_choice()

    # Perform operations
    sum_result, sub_result, multi_result = calculate_operations(num_1, num_2)

    print(
        f'First number: {num_1}\n'
        f'Second number: {num_2}\n\n'
        f'Sum result: {round(sum_result, 2)}\n'
        f'Subtraction result: {round(sub_result, 2)}\n'
        f'Multiplication result: {round(multi_result, 2)}'
    )
