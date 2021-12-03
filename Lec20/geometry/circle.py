import math as m
import pandas as pd

def perimeter(radius: float) -> float:
    """
    Выполняем подсчет длины окружности
    радиуса radius по формуле:
    2 * pi *radius
    """
    return 2 * m.pi * radius

def area(radius : float) -> float:
    """
    Выполняем подсчет площади окружности
    радиуса radius по формуле
    pi * radius ^2
    """
    return m.pi * (radius ** 2)

print("circle.py loaded")