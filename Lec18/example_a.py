# 1. Тип аргументов - required positional aruments 
# необходимые позициональные аргуементы
def sub_squared(a, b):
    res = a ** 2 - 2*a*b - b ** 2
    return res

print(sub_squared(3,4))
print(sub_squared(4,3))
#print(sub_squared(10, 10, 10))

# 2. Пример использования функций с rp-аргументами
def print_factorials(start, stop):
    for j in range(start, stop + 1):
        print(f"{j}! = {factorial(j)}")

def factorial(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def commbination(n ,m):
    return int(factorial(n) / (factorial(m) * (factorial(n-m))))

print_factorials(1, 15)


    