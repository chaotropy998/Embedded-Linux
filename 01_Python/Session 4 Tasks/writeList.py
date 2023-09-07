import os

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

file_path = "colors.txt"

if not os.path.exists(file_path):
    with open(file_path, "w"):
        pass
    
for i in color:
    with open(file_path, "a+") as file:
        file.write(i + "\n")
