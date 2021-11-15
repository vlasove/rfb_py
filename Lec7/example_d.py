# Пароль плохой если:
# 1) Первый не совпадает со вторым
# 2) Длина пароля строго меньше 10 символов
# 3) В пароле присутстввуют фразы "qwerty" или "asdfg"
attempts = 5

while True:
    if attempts <= 0:
        print("Кто ты такой чтобы меня запускать?")
        break

    password_1 = input()
    password_2 = input()

    if len(password_1) < 10:
        print("Длина должна быть больше 10 символов")
        # continue
    elif "qwerty" in password_1 or "asdfg" in password_1:
        print("Пароль содержит dummy-последовательность")
        # continue
    elif password_1 != password_2:
        print("Пароли не совпадают")
        # continue
    else:
        print("Ну какой же ты молодец!")
        break
    
    attempts = attempts - 1
    print("Осталось попыток:", attempts)

    
print("Вот тебе приз")