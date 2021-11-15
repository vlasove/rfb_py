# Задача F. Уравнение

coeff_a = float(input())
coeff_b = float(input())
coeff_c = float(input())

# ax^2 + bx + c = 0
if coeff_a == 0:
    # Линейное уравнение
    # 0x^2 + bx + c = 0
    # x = -c/b
    if coeff_b == 0:
        print("0")
    else:
        print("1")
else:
    # Квадратное уравнение
    D  = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if D > 0 :
        print("2")
    elif D == 0:
        print("1")
    else:
        print("0")