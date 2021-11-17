# Задача О. Знакопеременный ряд

n = int(input())
sum = 0
# n = 5
# 10, 20, 30, 40, 50 -> считываем из консоли
# Ряд: 10 - 20 + 30 - 40 + 50 = 30
# i  : 0    1    2    3    4

for i in range(n):
    numeric = int(input()) # 10, 20, 30....
    if i % 2 == 0:
        sum += numeric
    else:
        sum -= numeric

print(sum)