# Что надо делать? И чего делать не нужно?

# Правила именования скриптов и переменных
#   1) Скрипты именуем только с использованием латиниицы, _, и цифр
#   2) Перменные именуем ТОЛЬКО с использованием латиницы, _, и цифр
#   3) Переменные регистро-зависимые

# Правила присваивания переменных
lhs = 10
rhs = 20

lhs, rhs = 20, 10 # Множественное присваивание
# При множественном присваивании СПРАВА от знака = должно находиться
# ровно столько же значения, сколкьо СЛЕВА переменных


print(lhs, rhs)

# Пример
val_x , val_y = int(input()), int(input())
print("Sum:", val_x + val_y)


# Сквозное присваивание (ЭТО НЕ ЗНАЧИТ ЧТО ПРИСВАИВАНИЕ В PYTHON возвращает значение)
coordX = coordY = coordZ = 0
coordY = 20
print(coordX, coordY, coordZ)


# Как не надо делать?
expression = 25.2
if expression: # Python Expression Synonimic Casting
    print("If body!")

# Любое числовое значение кроме 0 - кастуется в True
# Любое числовое значение 0 - это False
# Любое строковое значение, кроме "" - кастуется в True
# Строковое значение вида "" - кастеутся в False
# None всегда False


# Как не надо делать 2?
value = 10 # Данная переменная видна в любой точке программы на СВОЕМ уровне отступов и глубже!
sample = ""

if True:
    value += 1
    print("First:", value)
    if True:
        sample = "some variable" # Создаю переменную на уровне отступа 2 (2 табуляции)
        value += 1
        print("Second:", value)

print("Origin:", value)
print("Sample:", sample) # Пытаюсь обратиться к переменной из более высокой области виидимости (с 0)


# Необходимо определять переменные ДО их использования в цикле или условном операторе,
# если данные переменные будут использоваться где-то еще