import os
from pathlib import Path

names = []
def all_dirs(directory):
    for file in os.listdir(directory):
        directory += '/'
        directory += file
        if os.path.isdir(directory):
            all_dirs(directory)

        else:
            names.append(file)
        directory = directory[:len(directory) - 1 - len(file)]

directory = 'C:/Users/ariam/PycharmProjects/bazaar_intern'
all_dirs(directory)
f = open("index.txt", "w")
for name in names:
    f.write(name)
    f.write("\n")