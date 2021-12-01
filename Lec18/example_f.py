# Континуальный аргумент - не именованный
def sum(*args):
    res = 0
    for elem in args:
        res += elem
    return res

print(sum(1))
print(sum(2,3))
print(sum(1,2,2,2,2,2,22,2,2,2,2,2,3))
print(sum(10, 10 ,10 ,10, 10, 10, 10, 10, 10, 10, 10, 10, 10))