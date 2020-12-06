""" Creates a txt for each file in data/src. """
import files
import normalize

for name in files.get_files():
    contents = normalize.get_normalized_text(name)
    filename = 'result-' + name
    with open(files.save_result(filename), 'w') as file_object:
        file_object.write(contents)