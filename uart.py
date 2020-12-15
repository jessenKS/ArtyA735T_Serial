import serial

print("Iniciando Serial...")
#use ttyUSB0 se for o caso, ou se for Windows, COMx.
fpga = serial.Serial('COM4',9600)
print("Serial Iniciada")

while 1:
    serialRead = fpga.read(20)
    print("Leitura: " + str(serialRead))