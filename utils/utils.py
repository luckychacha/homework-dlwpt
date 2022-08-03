import os

def chdir_to_file_dir(file_path):
    current_path = os.path.abspath(file_path)
    current_dir = os.path.abspath(os.path.dirname(current_path) + os.path.sep + '.')
    os.chdir(current_dir)
    print(os.getcwd())