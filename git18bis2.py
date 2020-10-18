from random import randint

noms = {"Cedric": 0, "Lison": 0, "Marc": 0}
run = True
while run:
    for nom in noms:
        if randint(1, 3) == 1:
            noms[nom] += randint(2, 5) / 2
        else:
            noms[nom] += randint(2, 5)
        if noms[nom] >= 100:
            run = False

for nom, value in noms.items():
    print(nom + " a parcourue " + str(value) + " m")
    print(f"{nom} a parcourue {value} m") #fstring, ne fonctione pas en microbit