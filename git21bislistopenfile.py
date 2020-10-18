numbers_file = open("file_2.txt", "r")
numbers_str = numbers_file.readlines()
numbers_file.close()

numbers = []

for number in numbers_str:
    numbers.append(int(number))

print(f"Min: {min(numbers)}, Max: {max(numbers)}")