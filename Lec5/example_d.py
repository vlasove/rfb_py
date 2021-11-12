# Напишем калькулятор который умеет складывать и вычитать 2 целых числа
num_a = int(input())
num_b = int(input())
sign = input()

if sign == "+":
    print(num_a + num_b)
elif sign == "-":
    print(num_a - num_b)
else:
    print("unsupported operation type")