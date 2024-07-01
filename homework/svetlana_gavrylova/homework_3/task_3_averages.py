from task_1_operations import get_numbers_from_user_choice


def calculate_arithmetic_mean(x, y):
    return (x + y) / 2


def calculate_geometric_mean(x, y):
    # Geometric mean cannot be calculated from negative numbers
    # If both numbers are negative, calculate the geometric mean
    if x < 0 and y < 0:
        return (x * y) ** 0.5
    # If one of the numbers is negative, raise an error
    elif x < 0 or y < 0:
        raise ValueError("Cannot calculate geometric mean for negative numbers.")
    else:
        return (x * y) ** 0.5


if __name__ == "__main__":
    # Get the numbers based on user choice
    num_1, num_2 = get_numbers_from_user_choice()
    error_message = ""

    arithmetic_mean = calculate_arithmetic_mean(num_1, num_2)

    # Geometric mean cannot be calculated from negative numbers
    try:
        geometric_mean = calculate_geometric_mean(num_1, num_2)
    except ValueError as ve:
        geometric_mean = None
        error_message = f"Error: {ve}"

    if geometric_mean is not None:
        geometric_mean = round(geometric_mean, 4)

    print(
        f'First number: {num_1}\n'
        f'Second number: {num_2}\n\n'
        f'Arithmetic mean: {round(arithmetic_mean, 4)}\n'
        f'Geometric mean: {geometric_mean}\n'
        f'{error_message}'
    )
