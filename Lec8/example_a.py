for i in range(0, 7, 2): # 0, 2, 4, 6
    print("Current:", i)

print("Done")
# range(start, stop, step)
# stop - не включается в диапазон

# В случае инкремента переменной (увеличения значения)
# stop должен быть всегда больше start, а step > 0
for i in range(10, 2, 3):
    print("Current in fail range:", i)


# В случае декремента переменной (уменьшения значения)
# start < stop, step <0
for i in range(10, -1, -1):
    print("Current in descend for loop:", i)

# start, stop, step - это только int
# из обязательныз - только stop!

# Если устраивает увеличение значения переменной на 1 (т.е. step=1), 
# его можно не писать (по умолчанию step=1)

for numeric in range(10, 16):
    print("Numeric:", numeric)

# Если устраивает начальное значение 0 (т.е. start=0)
# его можно не указывать (по умолчанию, start=0)
limit = 15
for j in range(limit):
    if j == 13:
        break
    if j % 2 == 0:
        continue
    print("J value:", j)

print("After loop")