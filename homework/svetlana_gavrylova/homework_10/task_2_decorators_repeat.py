def repeat_me(func):

    def wrapper(*args, **kwargs):

        count = kwargs['count']
        for _ in range(count):
            func(*args)

    return wrapper


def repeat_me_2(count):

    def decorator(func):

        def wrapper(*args):
            for _ in range(count):
                func(*args)

        return wrapper

    return decorator


@repeat_me
def example(text):
    print(text)


@repeat_me_2(count=3)
def example_2(text):
    print(text)


example('print me', count=2)
example_2('Parameterized decorator')
