import serial

port = "COM7"
conn = serial.Serial(port,115200)

while True:
    xy = input("Donne un x : ") + input("Donne un y : ")
    print(xy)
    conn.write(xy.encode())
