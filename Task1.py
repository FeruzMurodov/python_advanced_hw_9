from typing import Callable, Any
from functools import wraps


def how_are_you(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        input('How are you? ... ')
        print("And I'm not very good! Okay, keep your function!")
        result = func(*args, **kwargs)
        return result
    return wrapper

@how_are_you
def power():
    number = int(input('Enter a number: '))
    return int(number) ** 2

@how_are_you
def sum_numbers():
    a = int(input('Enter a number a: '))
    b = int(input('Enter a number b: '))
    c = int(input('Enter a number c: '))
    return sum((a,b,c))

if __name__ == '__main__':
    print(power())
    print(sum_numbers())