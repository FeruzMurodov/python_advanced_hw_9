from time import sleep


def moderator(func):
    def wrapper():
        sleep(2)
        return func()

    return wrapper


@moderator
def power():
    number = int(input('Enter a number: '))
    return int(number) ** 2

@moderator
def sum_numbers():
    a = int(input('Enter a number a: '))
    b = int(input('Enter a number b: '))
    c = int(input('Enter a number c: '))
    return sum((a, b, c))


if __name__ == '__main__':
    print(power())
    print(sum_numbers())
