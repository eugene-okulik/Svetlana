import sys


def fibonacci():
    x = 0
    y = 1
    while True:
        yield x
        temp = x
        x = y
        y = x + temp


if __name__ == "__main__":
    sys.set_int_max_str_digits(100000)
    count = 1
    for number in fibonacci():
        if count == 5 or count == 200 or count == 1000:
            print(f'Fibonacci number under # {count}: {number}')
        elif count == 100000:
            print(f'Fibonacci number under # {count}: {number}')
            break

        count += 1
