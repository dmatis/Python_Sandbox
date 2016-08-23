import os
import re
from sys import argv

script, directory = argv

def rename_files(directory):
    files = os.listdir(directory + "/")
    
    for f in files:
        new_name = ""
        for c in f:
            if not c.isdigit():
                new_name += f[f.index(c):]
                break
        old_file = os.path.join(os.getcwd(),directory,f)
        new_file = os.path.join(os.getcwd(),directory,new_name)
        os.rename(old_file, new_file)

rename_files(directory)
