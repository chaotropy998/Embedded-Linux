import os

def count_lines(filename):
    try:  
        with open(filename, "r") as file:
            lines = file.readlines()
            lines_count = len(lines)
        return lines_count
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error has occurred: {e}"
    
    
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = input("Enter the .txt file name: ")
file_path = os.path.join(script_dir, file_name)    

lines_count = count_lines(file_path)

if isinstance(lines_count, int):
    print(f"The file {file_name} has {lines_count} lines.")
else:
    print(lines_count)