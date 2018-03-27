import numpy as np
import os


files = []
for file in os.listdir("."):
    if file.endswith(".npz"):
        files.append(file)
files.sort()


def load_data(filename):
    table = {}
    with np.load(filename) as data:
        for key in data.keys():
            table[key] = data[key]
    return table

print(files)

Table = load_data(files[0])
print(Table.keys())
for file in files[1:]:
    print(file)
    data = load_data(file)
    for key in data.keys():
        Table[key] = np.append(Table[key], data[key])

#a = load_particle_array("data_10Hz_123.npz")
print(len(Table["orbit_x"]))