# while expression:
#     body

# Условно бесконечный цикл while

while True: # expression = True
    name = input()
    if name == "": # пустая строка == нажать Enter на вводе
        break      # break можно использовать только внутри тела цикла
    print("Inputted name:", name)

print("DONE")



while True: # expression = True
    numeric = int(input())
    if numeric == 0: 
        break      # break можно использовать только внутри тела цикла
    print("Inputted value:", numeric)

print("DONE")


while True:
    value = input()
    if value == "":
        print("Enter another value!")
        continue   # Останавливает текущую итерацию и передает урпавление следующей итерации цикли

    numeric_value = int(value)
    if numeric_value < 0:
        break
    print("Numeric value:", numeric_value)