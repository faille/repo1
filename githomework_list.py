numbers = []

while sum(numbers) < 20:
    number = input("Donne moi un chiffre: ")
    number = int(number)
    numbers.append(number)

print("Nombre de chiffre entrés: " + str(len(numbers)))
print("Valeur minimum entrée: " + str(min(numbers)))
print("Valeur maximum entrée: " + str(max(numbers)))