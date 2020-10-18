mot = ""
for i in range(6):
    lettre = input("Donner une lettre : ")
    while lettre[1:] != "":
        lettre = input("Donner 1 lettre pas + : ")
    mot += lettre
print(mot)