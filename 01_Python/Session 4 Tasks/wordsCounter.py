import os

def count_words(filename):
    try:  
        with open(filename, "r") as file:
            f = file.read()
            words = f.split()
            words_count = len(words)
        return words_count
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error has occurred: {e}"
    
    
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = input("Enter the .txt file name: ")
file_path = os.path.join(script_dir, file_name)    

words_count = count_words(file_path)

if isinstance(words_count, int):
    print(f"The file {file_name} has {words_count} words.")
else:
    print(words_count)