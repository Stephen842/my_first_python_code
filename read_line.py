from os import strerror

try:
    char_counter = 0
    line_counter = 0
    stream = open("file.txt", "rt") #input filename here
    line = stream.readline()

    while line != "":
        line_counter += 1
        for char in line:
            print(char, end="")
            char_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file", char_counter)
    print("lines in file ", line_counter)

except IOERROR as e:
    print("I/O An error occurred", strerr(e.errno))
