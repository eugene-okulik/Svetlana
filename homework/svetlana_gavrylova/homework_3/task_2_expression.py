from task_1_operations import get_numbers_from_user_choice


# Function to perform the following expression: x − y / 1 + xy
def calculate_expression(x, y):
    return (x - y) / (1 + x * y)


if __name__ == "__main__":
    # Get the numbers based on user choice
    num_1, num_2 = get_numbers_from_user_choice()

    # Perform operations
    expression_result = calculate_expression(num_1, num_2)

    print(
        f'First number: {num_1}\n'
        f'Second number: {num_2}\n\n'
        f'Expression result: {round(expression_result, 4)}'
    )
