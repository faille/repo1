import serial

port = "COM7"
conn = serial.Serial(port, 115200)


msg = input()
print(msg)
conn.write(msg.encode())
