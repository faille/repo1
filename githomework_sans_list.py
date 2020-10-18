sum_numbers = 0
max_value = None
min_value = None
n_numbers = 0

while sum_numbers < 20:
    number = input("Donne moi un chiffre: ")
    number = int(number)

    if n_numbers == 0:
        max_value = number
        min_value = number
    else:
        if number < min_value:
            min_value = number
        elif number > max_value:
            max_value = number

    n_numbers += 1
    sum_numbers +=  number

print("Nombre de chiffre entrés: " + str(n_numbers))
print("Valeur minimum entrée: " + str(min_value))
print("Valeur maximum entrée: " + str(max_value))