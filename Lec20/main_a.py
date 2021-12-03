# Импортирование в совмещающее пространство имен
# from <module> import <obj_name>

from sample import add, numerics, MAX_VALUE

def add(a : int, b : int) -> int:
    """
    a^2 + b^2
    """
    return a ** 2 + b ** 2




print(add(10, 20))