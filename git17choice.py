from random import randint
from random import choice

mots = ["disorder", "enemy", "humanity", "is", "of", "the", "true"]
phrase = ""
while mots:
    mot = choice(mots)
    mots.remove(mot)
    phrase += mot + " "
print(phrase)