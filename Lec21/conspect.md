## Лекция 21. Стандарты и утилиты

* **ВАЖНО** - на Python очень просто написать УЖАСНЫЙ И НЕПОНЯТНЫЙ КОД!
* Самое важное требование к коду на Python - это то, чтобы он был ПОНЯТНЫМ!

### 1. Стандарты
* `PEP8` - основной стандарт написания кода на `Python` (текущий). В нем присутствует куча ссылок на более детальные стандарты.

* Со временем начнете его понимать и нужно стараться соблюдать все его принципы!

### 2. Автоматизированные утилиты
* Утилиты, которые помогают приблизить ваш код к стандартному

* Пример, рассмотрим файл `main.py`:
```
def add(a,b):
                    return a +                b

def sub(c, c1):



 return c + c1


def mult(x,y         ):
    return                         x                        *                     y


def деление(o, o2):
 return o // o2


def main():
    a,b = int(input().strip()), int(input().strip())
    result = add(a,b) + add(b,a) + sub(add(a,a), mult(b,b)) - деление(b,a) ** 2 + add(a,b) + add(b,a) + sub(add(a,a), mult(b,b)) - деление(b,a) ** 2
    print(result)

if __name__ == '__main__':
    main() 
```

* 1-ая проблема - плохое форматирование (отступы, пробелы, перенос, лишние пустые строки и т.д.)
    * Решение проблемы `pip install black` - `black` инструмент автоформатирования кода, запускается командой `black module_name.py` 
    * Еще есть старый неадекватный `autopep8` , по умолчанию в `PyCharm`
* 2-ая проблема - читабельность отсутствует
    * Решение этой проблемы `pip install pylint` . Это линтер-советник, который подскажет, где написано не по стандарту. Называют такой инструмент *СИНТАКСИЧЕСКИЙ АНАЛИЗАТОР)
    * Запускается `pylint module_name.py`
    * После всех исправлений вновь запускаем `black module_name.py`

* 3-ая проблема - существует стандарт на писание `docstrings`:
    * Решение `pip install docformatter`
    * Использование `docformatter -i main.py`
* 4-ая проблема - неупорядоченные `imports` 
    * Решение `pip install isort`
    * `isort module.py`
* 5-ая проблема - использование функций не с теми аргументами (не с теми типами)
    * Решение `pip install mypy`
    * `mypy module.py`

### Итог
По итогу получим +- вменяемый код:
```
"""Модуль содержащий набор функций для простейших операций с целыми числами."""

import math
import sys
from typing import List


import calculator


def add(x_arg: int, y_arg: int) -> int:
    """Сложение x_arg + y_arg."""
    return x_arg + y_arg


def sub(x_arg: int, y_arg: int) -> int:
    """
    Вычитание x_arg - y_arg.
    """
    return x_arg + y_arg


def mult(x_arg: int, y_arg: int) -> int:
    """
    Умножение x_arg * y_arg.
    """
    return x_arg * y_arg


def div(x_arg: int, y_arg: int) -> int:
    """Деление нацело x_arg // y_arg."""
    return x_arg // y_arg


def main() -> None:
    """Основная точка входа в программу."""
    num_a, num_b = int(input().strip()), int(input().strip())
    result = (
        add(num_a, num_b)
        + add(num_b, num_a)
        + sub(add(num_a, num_a), mult(num_b, num_b))
        - div(num_b, num_a) ** 2
        + add(num_a, num_b)
        + add(num_b, num_a)
        + sub(add(num_a, num_a), mult(num_b, num_b))
        - div(num_b, num_a) ** 2
    )
    print(result)
    


if __name__ == "__main__":
    main()
```

# Альтернактивный запуск
`utility module.py` или `python -m utility module .py`