import serial

#use ttyUSB0 se for o caso, ou se for Windows, COMx.
fpga = serial.Serial('COM4',9600)

while 1:
    teste = fpga.read(20)
    print(teste)