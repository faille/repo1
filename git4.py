import serial #il faut dabord flacher git3 et puis ici

port = "COM7"
conn = serial.Serial(port,115200)

def ask_position():
    x = int(input("Donne un x : "))
    y = int(input("Donne un y : "))
    data = str(x) + str(y)
    return data

PLAYER1 = 1
PLAYER2 = 2
players = [PLAYER1, PLAYER2]
while True:
    for player in players:
        print("Player " + str(player) + ": ")
        data = ask_position() + str(player)
        conn.write(data.encode())

        incoming = conn.readline()
        if incoming.decode().strip() == "OK":
            print("Pixel bien placer")
        else:
            print("ERREUR")
