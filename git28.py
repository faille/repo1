from random import randint

x = randint(1, 10)
y = randint(1, 10)
result = int(input(f"conbien fait {x} * {y} = "))
if x * y == result:
    print("correct!")
else:
    print(f"La réponse était {x * y}")