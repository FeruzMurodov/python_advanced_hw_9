from collections.abc import Callable
from functools import wraps
import csv
import json
from pathlib import Path


def counter(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"The function '{func.__name__}' was called {wrapper.count} times")
        return result
    wrapper.count = 0
    return wrapper


@counter
def json_to_csv(path: Path):
    with open(path, 'r', encoding='utf-8') as fr:
        data = json.load(fr)
        print(data)
    with open(f'{path.stem}.csv', 'w', newline='', encoding='utf-8') as fw:
        csv_write = csv.DictWriter(fw, fieldnames=['name', 'price', 'quantity'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(data)

@counter
def power():
    number = int(input('Enter a number: '))
    return int(number) ** 2

if __name__ == '__main__':
    json_to_csv(Path(r'D:\Python projects\Advanced_python_course\HW_9\products.json'))
    print(power())
    print(power())
    print(power())
    json_to_csv(Path(r'D:\Python projects\Advanced_python_course\HW_9\products.json'))

