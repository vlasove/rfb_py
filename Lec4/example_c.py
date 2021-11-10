# Вхождение подстроки в строку

password = input()
DANGER_SUB_STRING = "qwe"

if len(password) < 5:
    print("Это очень короткий пароль!")
elif DANGER_SUB_STRING in password:
    print("Пароль содержит глупую комбинацию!")
else:
    print("Это очень хороший пароль!")