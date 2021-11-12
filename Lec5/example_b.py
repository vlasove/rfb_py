# Обратные числа
numeric = float(input())

if abs(numeric) < 0.0001:
    print("ОЧЕНЬ МНОГО")
else:
    print(1/numeric)