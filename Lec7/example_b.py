# Задача D. Ход конем
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

vertical_exapression = abs(y1 - y2) == 2 and  abs(x2 - x1) == 1
horizontal_expression = abs(y1 - y2) == 1 and  abs(x2 - x1) == 2

if vertical_exapression or horizontal_expression:
    print("ДА")
else:
    print("НЕТ")