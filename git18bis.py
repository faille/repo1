from random import randint

noms = {"Cedric": 0, "Lison": 0, "Marc": 0}
run = True
while run:
    for nom in noms:
        noms[nom] += randint(2, 5)
        if noms[nom] >= 100:
            run = False
for nom, value in noms.items():
    print(nom + " a parcourue " + str(value) + " m")