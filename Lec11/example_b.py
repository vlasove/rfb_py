# Строки - неизменяемые!
message = "Gello"
#message[0] = "H"
message = "H" + message[1:]
print(message)


# Смена регистра вверх
phrase = "AbCdEfG"
upper_phrase = phrase.upper()
print("Phrase upper:", upper_phrase)
print("Phrase origin:", phrase)

# Смена регистра вниз
lower_phrase = phrase.lower()
print("Phrase lower:", lower_phrase)

# Смена регистра capitalize()
capitalize_phrase = phrase.capitalize()
print("Phrase capitalize:", capitalize_phrase)