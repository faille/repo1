grand = None
petit = None
fichier = open("file_2.txt", "r")
for number in fichier.readlines():
    number = int(number)
    if petit == None:
        grand = number
        petit = number
    else:
        if number < petit:
            petit = number
        elif number > grand:
            grand = number
print(f"Le chiffre le plus grand : {grand} et le plus petit : {petit}")
fichier.close()