# Break

numeric = 10
sum = 0  # Счетчик / накопитель/ штука


while numeric > 0:
    print("Current numeric:", numeric)
    print("Current sum:",)
    sum = sum + numeric
    
    if sum > 30:
        break # Используется

    numeric = numeric - 1

    
    

print("Sum is:", sum)