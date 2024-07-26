def finish_me(func):

    def wrapper(*args):
        result = func(*args)
        print(f'Finished')
        return result

    return wrapper


@finish_me
def my_func(a, b):
    print(a + b)


@finish_me
def example_1(text):
    print(text)


my_func(1, 2)
example_1('Hello, World!')
