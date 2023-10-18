import os

os.makedirs("directory_1/directory_2/directory_3")
os.chdir("directory_1")
print(os.getcwd)
os.chdir("directory_2")
print(os.getcwd)
