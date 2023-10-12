from os import strerror

try:
    counter = 0
    stream = open("file.txt", "rt") #input the name of the file
    content = stream.read()

    for char in content:
        print(char, end="")
        counter += 1
    stream.close()
    print("\n\nCharacters in file", counter)

except IOERROR as e:
    print("I/O error occurred ", strerr(e.errno))
