from os import strerror

try:
    file = open("new_file.txt", "wt") # A new file is been created
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()

except IOERROR as e:
    print("I/O An error occurred", strerr(e.errno))
