# Задача H
message = input()
word_set = set(["да", "Да", "дА", "ДА", "ад", "аД", "АД", "Ад"])

if (message[0] + message[-1]) in word_set:
    print("СОГЛАСЕН")
else:
    print("НЕ СОГЛАСЕН")