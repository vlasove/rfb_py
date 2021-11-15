# Допустим на вход программе поступает 5
# Требует найти максимальное
# Гарантируется, что все числа положительные и не превышают 10 ^ 5

count = 1
current_max = -1000
current_min = 10 ** 7

while True:
    if count > 5:
        break
    numeric = int(input())
    count += 1

    if numeric > current_max:
        current_max = numeric

    if numeric < current_min:
        current_min = numeric

print("Current max is:", current_max)
print("Current min is:", current_min)