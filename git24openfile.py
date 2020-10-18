fichier = open("file_2.txt", "r")
numbers = fichier.read()
fichier2 = open("file_5.txt", "w")
fichier.close()

continuer = True
donner = ""
while continuer:
    nom = input("Donner Votre nom : ")
    if nom == "end":
        continuer = False
    else:
        donner += nom + "\n"
fichier2.write(numbers + donner)

fichier2.close()