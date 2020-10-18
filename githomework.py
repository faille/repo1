somme = 0
nbrchiffre = 0
grand = 0
petit = 20
while somme < 20:
    chiffre = int(input("entré un chiffre : "))
    somme += chiffre
    nbrchiffre += 1
    grand = max(grand, chiffre)
    petit = min(petit, chiffre)
    if petit > 19:
        petit = grand
print("Vous aver entré " + str(nbrchiffre) + " chiffre, le plus grand : " + str(grand) + " et le plus petit : " + str(petit))