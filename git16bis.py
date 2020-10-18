from random import choice

possibilities = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"]

errors = 0

for n in range(5):
    character = choice(possibilities)

    answer = input("Taper la lettre '" + character + "': ")
    while(answer !=  character):
        errors += 1
        answer = input("Taper la lettre '" + character + "': ")

print("Vous avez fait " + str(errors) + " erreurs.")