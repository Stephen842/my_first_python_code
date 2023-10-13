from os import strerror

data = bytearray(20)
for i in range(len(data)):
    data[i] = 20 - i

try:
    bin_file = open("file.bin", "wb") # input filename
    bin_file.write(data)
    bin_file.close()

except IOERROR as e:
    print("I/O An error occurred", strerr(e.errno))
