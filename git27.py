def table(multiplication):
    for i in range(11):
        print(f"{i} * {multiplication} = {i * multiplication}")
multiplication = int(input("Quel table de multiplication? : "))
table(multiplication)