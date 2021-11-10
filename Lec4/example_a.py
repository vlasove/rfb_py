# Классический синтаксис условного оператора
# if expression:
#     body


# if expression:
#     body_if
# else:
#     body_else

# if expression1:
#     body_1
# elif expression2:
#     body_2
# elif expression3:
#     body_3
# else:
#     body_else


login = input()
age = int(input())

if age >= 18 and len(login) > 3:
    print("<h1>Welcome Page</h1>")
    print("<p>Confirm your account by...<p>")

print("Program done!")

# Какие еще есть операции сравнения над числовыми типами? (int/float)
print(11 > 10)
print(12.5 > 12) # Здесь 12 неявно преобразуется в 12.0
print(10 < 22)
print(11 >= 11)
print(6 <= 10)
print(10 == 10) # True
print(12 != 11) # True 