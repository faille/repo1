<<<<<<< HEAD
l = list(range(1, 1000))
m = []

for value in l:
    if value % 10 == 0:
        m.append(value)

m = [value for value in l if value % 10 == 0]
print(m)

###

l = ["annanas"," gâteau", "chataigne", "pétanque", "marguerite", "saperlipopette", "tahin"]
m = [word[0].upper() for word in l if "n" in word]
print(m)

###

students = {"Albert": 10, "Leopold": 30, "Baudouin": 20, "Gonzague": 76, "Cunégonde": 76, "Ginette": 59, "roberte": 99}
bestof = [name for name, score in students.items() if score >= 50]
print(bestof)
=======
def table(multiplication):
    for i in range(11):
        print(f"{i} * {multiplication} = {i * multiplication}")
multiplication = int(input("Quel table de multiplication? : "))
table(multiplication)
>>>>>>> 79fc7ba1fd28b132acd0dc114ca8bc70923539df
