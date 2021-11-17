# Задача О. Знакопеременный ряд

n = int(input())
sum = 0
# n = 5
# 1,2,3,4,5
# Ряд: 1 - 2 + 3 - 4 + 5
# i  : 0   1   2   3   4

for i in range(n):
    numeric = int(input())
    if i % 2 == 0:
        sum += numeric
    else:
        sum -= numeric

print(sum)