# Вещественные числа
a_float = float(input()) # float("11.44")
b_float = float(input()) # float("20.5")

# Вывод в StdOut
print(a_float, b_float)
# Сам тип - команда type()
print("Type of a_float:", type(a_float))

# Сложение
sum_float = a_float + b_float
print("Sum:", sum_float)

# Вычитание
sub_float = a_float - b_float
print("Sub:", sub_float)


# Умножение
mult_float = a_float * 10 # Пример неявного приведения 10 к float(10) == 10.0
print("Mult:", mult_float)

# Деление - всегда вещественное число возвращает
div_float = a_float / b_float
print("Div result 10/20:", div_float)
print("Div result 20/10:", b_float / a_float)


# Деление нацело (целочиесленное деление)
div_round_float = 12.5 // 3.5 
print("Div round 12.5 // 3.5 :", div_round_float)


# Взятие остатка от деления
mod_float = 7.5 % 2.3
print("Mod of 7.5 by 2.3:", mod_float)


# Вовзведение в степень
pow_float = 2.5 ** 0.5 # 2.5 ^ 0.5
print("Val of 2.5^0.5:", pow_float)



# Приведение из/в int
a_int = 10
from_a_int_to_float = float(a_int) # явное приведение типа в float

print(from_a_int_to_float)


c_float = -2222.5555555
from_c_float_to_int = int(c_float) # явное приведение типа в int

print(from_c_float_to_int)