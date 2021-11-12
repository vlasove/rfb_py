# Взятие остатка от деления
a_int = 8 
b_int = 9

print("Остаток от деления 8 на 2:", a_int % 2)
print("Остаток от деления 9 на 2:", b_int % 2)

res_a_int = a_int % 2
if res_a_int == 0:
    print("ЧЕТНОЕ")
else:
    print("НЕЧЕТНОЕ")


# С вероятности
p1 = float(input())
p2 = float(input())


print(1 - p1 * p2)
