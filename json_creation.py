""" Creates and saves a JSON file containing all texts defined in files.py.
This JSON complies to the required input format as given at 
https://collatex.net/doc/#json-input. """
import files
import json
import normalize

contents = []

for name in files.get_files():
    witness = {'id': name, 'content': normalize.get_normalized_text(name)}
    contents.append(witness)

result = {'witnesses': contents}
filename = 'result.json'

with open(files.save_result(filename), 'w') as file_object:
    file_object.write(json.dumps(result))
