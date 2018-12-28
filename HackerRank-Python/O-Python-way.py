import os
import subprocess

path = 'C:\TEMP'
files = []

def tree_func(root):
    for root, dirs, files in os.walk(root):
        for f in files:
            line = os.path.join(root, f)
            if "log" in line:
                print(line)
            else:
                print("Doesn't match!")

# files = list(tree_print(path).split("\n"))
# print(type(files))

tree_func(path)
# for line in files:
#     if "*log*" in line:
#         print(line)