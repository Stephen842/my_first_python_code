import os

os.makedirs("my_first_python_dir/my_second_py_dir")
os.chdir("my_first_python_dir")
print(os.listdir())
