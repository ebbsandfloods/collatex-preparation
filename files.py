""" Deals with file management. """
import os

def get_files():
    src_dir = './data/src'
    return [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

def make_data_dir(dirname):
    if os.path.exists('data/' + dirname):
        pass
    else:
        os.mkdir('data/' + dirname)

def save_result(filename):
    make_data_dir('results')
    return os.path.join('./data/results', filename)

def get_file_path(filename):
    src_dir = './data/src'
    return os.path.join(src_dir, filename)
