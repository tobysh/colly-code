import os 
import sys

def get_path(folder:str="assets", file_name="greetings.txt"):
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = os.path.join(script_directory,folder,file_name)
    return file_path


