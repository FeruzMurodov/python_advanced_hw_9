from functools import cache


@cache
def fibonacci(number: int):
    print(f'Calculating fibonacci for number {number}...')
    if number in (1, 2):
        return 1
    temp1 = int(fibonacci(int(number - 1)))
    temp2 = int(fibonacci(int(number - 2)))
    result = temp1 + temp2
    return result


if __name__ == '__main__':
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(3))
