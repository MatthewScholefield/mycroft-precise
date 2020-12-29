import os
import shutil

def create_dir(filepath):
    try:
        os.mkdir(filepath)
    except OSError:
        raise Exception("Creation of the directory %s failed" % filepath)
    else:
        print("Successfully created the directory %s " % filepath)

def numConcat(num1, num2): 

     return f"{num1}{num2}"

import errno
 
def copyfolder(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)