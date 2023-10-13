data = bytearray(20)

for i in range(len(data)):
    data[i] = 20 - i

for j in data:
    print(hex(j))
