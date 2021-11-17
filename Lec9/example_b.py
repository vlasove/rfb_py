# Задача R.  Игра в слова


words_set = set()

for _ in range(int(input())):
    word = input()
    words_set.add(word)

if input() in words_set:
    print("НЕ ЗАСЧИТАНО")
else:
    print("ЗАСЧИТАНО")