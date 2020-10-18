numbers_file = open("file_7.txt")
lines = numbers_file.readlines()
numbers_file.close()

results_file = open("file_7somme.txt", "w")

for line in lines:
    line = line.split(" ")
    if line[-1] == '\n':
        line =  line[:-1]

    result = 0

    for number in line:
        number = int(number)
        result += number
    results_file.write(str(result) + "-")

results_file.close()