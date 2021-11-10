## Лекция 3. Базовые типы данных

**Задача** - рассмотреть 5 базовых типов данных в `Python`.

Все базовые типы:
* `int` - целые числа
* `float` - вещественные числа
* `bool` - логический тип
* `str` - строковый тип
* `NoneType` - тип "без значения"

### 1. Целые числа и операции
```
# Целые числа
a_int = 10
b_int = 20 

# Вывод в StdOut
print(a_int, b_int)
# Сам тип - команда type()
print("Type of a_int:", type(a_int))
```

#### Операции
```
# Сложение
sum_int = a_int + b_int
print("Sum:", sum_int)

# Вычитание
sub_int = a_int - b_int
print("Sub:", sub_int)


# Умножение
mult_int = a_int * b_int
print("Mult:", mult_int)

# Деление - всегда вещественное число возвращает
div_int = a_int / b_int
print("Div result 10/20:", div_int)
print("Div result 20/10:", b_int/a_int)


# Деление нацело (целочиесленное деление)
div_round_int = -4 // 3 
print("Div round -4 // 3:", div_round_int)


# Взятие остатка от деления
mod_int = 7 % 5
print("Mod of 35 by 12:", mod_int)


# Вовзведение в степень
pow_int = 2 ** 5 # 2 ^ 5
print("Val of 3^11:", pow_int)
```

#### Считывание
Считывание через явное приведение типов:
```
val_str = "10"
val_int = int(val_str)
```

Для явного приведения строкового значения к целочисленному необходимо:
* 1) чтобы строка состояла ТОЛЬКО из символов цифр
* 2) допускается ОДИН знак `-` в самом начале строки

```
a_int = int(input()) # int("10")
b_int = int(input()) # int("20")
...
```