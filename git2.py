import serial #il faut dabord flacher git1 et puis ici

port = "COM7"
conn = serial.Serial(port,115200)

while True:
    print("1. Ecrire")
    print("2.Lire")
    choice = input("choix: ")

    if choice == "1":
        message = input("Message: ")
        channel = input("Channel: ")
        if int(channel) < 10 :
            channel = "0" + channel

        message = channel + message
        conn.write(message.encode())
    else:
        while True:
            data = conn.readline()
            if data:
                print(data.decode())
