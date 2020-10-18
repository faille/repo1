from random import randint

words = ["disorder", "enemy", "humanity", "is", "of", "the", "true"]

sentence = ""

while words:
    index = randint(0, len(words)-1)
    word = words.pop(index)
    sentence += word + " "

print(sentence)