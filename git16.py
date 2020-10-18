from random import choice

possibilities = [
    "a", "b", "c", "d", "e", 
    "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", 
    "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z"]

character = choice(possibilities)

answer = input("Taper la lettre '" + character + "': ")
while(answer !=  character):
    answer = input("Taper la lettre '" + character + "': ")