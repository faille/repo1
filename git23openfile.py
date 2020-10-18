fichier = open("file_2.txt", "r")
numbers = fichier.readlines()
fichier.close()
fichier2 = open("file_4.txt", "w")

for number in numbers:
    number = int(number)
    if number % 7 == 0:
        fichier2.write(str(number) + "\n")

fichier2.close()