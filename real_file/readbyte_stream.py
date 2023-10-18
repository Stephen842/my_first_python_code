from os import strerror

data = bytearray(20)

try:
    bin_file = open("file.bin", "rb")
    data = bytearray(bin_file.readinto())
    bin_file.close()

    for b in data:
        print(hex(b), end=" ")

except IOERROR as e:
    print("I/O An error occurred", strerror(e.errno))
