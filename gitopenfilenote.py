fichier = open("gitopenfile.txt", "r") #r = read
#fichier = open("gitopenfile.txt") #r par defaut
#fichier = open("gitopenfile.txt", "w") #w = write #en l'ouvrant il clear le fichier
#fichier = open("file_3.txt", "a") #a = append rajoute fin fichier

result = 0
#print(fichier.readline()) #read affiche toute la page, readline 1 ligne (il consomme la donner)
#print(fichier.readline()) #readline 2eme ligne

#print(fichier.readline()) #readline 1 ligne
#print(fichier.read()) #lis tout le fichier sauf se qui a déja été lus

#print(fichier.readlines())

#for line in fichier.readlines():
#    print(line)

for number in fichier.readlines():
    number = int(number)
    result += number
    #print(number, end="")
    #fichier.write(number)

print(result)
#print(f":-=-=-=-=-=-=-=-=-=-=-=-=-=-:".center(75))

fichier.close()