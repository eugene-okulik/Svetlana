import math

from task_1_operations import get_numbers_from_user_choice


def find_hypotenuse_and_area(leg_1, leg_2):
    if leg_1 <= 0 or leg_2 <= 0:
        raise ValueError("Legs of the triangle must be positive numbers and cannot be zero.")

    # Calculate the hypotenuse
    hypo_res = math.sqrt(leg_1 ** 2 + leg_2 ** 2)
    # Calculate the area
    area_res = (leg_1 * leg_2) / 2

    return hypo_res, area_res


if __name__ == "__main__":
    # Get the numbers based on user choice
    num_1, num_2 = get_numbers_from_user_choice()
    try:
        hypotenuse, area = find_hypotenuse_and_area(num_1, num_2)
        print(
            f'First leg of the triangle: {num_1}\n'
            f'Second leg of the triangle: {num_2}\n\n'
            f'Hypotenuse: {round(hypotenuse, 2)}\n'
            f'Area: {round(area, 2)}'
        )
    except ValueError as ve:
        print(f"Error: {ve}")
