PLAYER_1 = 'X'
PLAYER_2 = 'O'
x = 0
y = 0
board = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]]

def display():
    txt = ""
    for row in board:
        for data in row:
            txt += data
        txt += "\n"
    print(txt)

def place(carac, x, y):
    board[y][x] = carac

def give(x, y):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return None
    return board[y][x]

def is_full():
    for x in board:
        for y in x:
            if y == ".":
                return False
    return True

def init():
    for n in range(len(board)):
        del board[0]
        board.append(['.', '.', '.', '.', '.'])
    save()
    return board

def play():
    while True:
        x = int(input("x : "))
        y = int(input("y : "))
        if x >= 0 and x <=4 and y >= 0 and y <=4:
            if board[y][x] == ".":
                return x, y
            else:
                print("coordonée déja prise : ")
        else:
            print("coordonée incorrect : ")

def check_victory(x, y):
    player = give(x, y)

    if give(x + 1, y) == player:
        if give(x + 2, y) == player:
            return True
        if give(x - 1, y) == player:
            return True
    if give(x - 1, y) == player and give(x - 2, y) == player:
        return True

    if give(x, y + 1) == player:
        if give(x, y + 2) == player:
            return True
        if give(x, y - 1) == player:
            return True
    if give(x, y - 1) == player and give(x, y - 2) == player:
        return True
    return False

def player_plays(player):
    display()
    x, y = play()
    place(player, x, y)
    victory = check_victory(x, y)
    if is_full():
        init()
    return victory

def save():
    data = ""
    for row in board:
        for item in row:
            data += item
        data += '\n'
    data = data[:-1]

    oxo_data = open("oxo.txt", "w")
    oxo_data.write(data)
    oxo_data.close()

def load():
    oxo_data = open("oxo.txt")
    data = oxo_data.read()
    oxo_data.close()
    data = data.split('\n')

    for row in data:

        del board[0]
        new_row = []

        for item in row:
            new_row.append(item)
        board.append(new_row)

victory = False
load()
while not victory:
    save()
    print("Player 1:")
    victory = player_plays(PLAYER_1)

    if victory:
        display()
        print("Player 1 a gagné")
        init()
    else:
        print("Player 2:")
        victory = player_plays(PLAYER_2)
        if victory:
            display()
            print("Player 2 a gagné")
            init()