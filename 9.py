import os
script_dir = os.path.dirname(__file__)
rel_path = "data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
file = open(abs_file_path, "rt")

data = file.read()
words = data.split()

print('Number of words in text file :', len(words))