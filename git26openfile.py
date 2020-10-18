fichier = open("file_8.txt", "r")
numbers = fichier.readline()
fichier.close()

list = numbers.split(" ")
print(list)

index = int(input("Où mettre la donner? : "))
donner = input("Que voulez-vous mettre? : ")
list.insert(index, donner)
print(list)

fichier = open("file_8.txt", "w")
result = ""

for i in list:
    result += i + " "

fichier.write(result[:-1])
fichier.close()
#2 3 5 7