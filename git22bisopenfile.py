fichier = open("file_3.txt", "a")

mot = ""
for i in range(6):
    lettre = input("Donner une lettre : ")
    while lettre[1:] != "":
        lettre = input("Donner 1 lettre pas + : ")
    mot += lettre
    fichier.write(lettre)
print(mot)

fichier.close()