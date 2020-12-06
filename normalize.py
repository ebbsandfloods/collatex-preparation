import files
import re

def get_normalized_text(filename):
    """ Removes all punctation from a given file and returns a single line
    string representation of it. """
    with open(files.get_file_path(filename)) as file_object:
        contents = file_object.read()
        contents = contents.strip()
        contents = re.sub(r'[.,!;?"”“]', '', contents)
        contents = re.sub(r'[-—]', ' ', contents)
        return re.sub(r'\s+', ' ', contents)
