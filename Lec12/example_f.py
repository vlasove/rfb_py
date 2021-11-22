# Задача N.
n = int(input())
numerics = []

for _ in range(n):
    number = int(input())
    numerics.append(number)

a = int(input()) # От какого индекса считать сумму
b = int(input()) # До какого индекса считать сумму

print(sum(numerics[a-1:b]))