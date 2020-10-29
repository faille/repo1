<<<<<<< HEAD
fichier = open("file_9gateau-citron-pomme-de-terre.txt", "r")
recette = fichier.read()
fichier.close()

print(recette)
lignes = recette.split("\n")

mots = []
for i in lignes:
    mots += i.split(" ")

supp = [";", ":", ".", ",", "?", "!", "-", "0", "1",
        "2", "3", "4", "5", "6", "7", "8", "9"]
motsclean = []
for mot in mots:
    for i in supp:
        if i in mot:
            mot = mot.replace(i, "")
    motsclean.append(mot)

motsclean = [mot for mot in motsclean if mot != ""]
print(motsclean)


mots_finissant_par_e = [mot for mot in motsclean if mot[-1] == 'e']

print(f"Nombre de mots finissant par 'e': {len(mots_finissant_par_e)}")

mots_commençant_par_f = [mot for mot in motsclean if mot[0] == 'f']

mot_le_plus_long = None

for mot in mots_commençant_par_f:
    if mot_le_plus_long == None:
        mot_le_plus_long = mot
    elif len(mot) > len(mot_le_plus_long):
        mot_le_plus_long = mot

print(f"Le mot le plus longs commençant par f est: {mot_le_plus_long}")
=======
from random import randint

x = randint(1, 10)
y = randint(1, 10)
result = int(input(f"conbien fait {x} * {y} = "))
if x * y == result:
    print("correct!")
else:
    print(f"La réponse était {x * y}")
>>>>>>> 79fc7ba1fd28b132acd0dc114ca8bc70923539df
