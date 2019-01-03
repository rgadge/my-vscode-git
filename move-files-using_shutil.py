#!/bin/python3

import os
import subprocess
import shutil

#https://www.pythoncentral.io/how-to-recursively-copy-a-directory-folder-in-python/

path = '/data/app_data/'

def is_file_open(file_name):
    """This function will take a path as input and will check if there any files open(being used) within that folder,
    and will return True in case the file is open, or else return False"""
    print("Checking ", file_name, " - ",)
    process = subprocess.Popen(["/sbin/lsof", file_name], stdout=subprocess.PIPE)
    process.communicate()[0]
    if process.returncode == 0:
        print("Open!")
        return True
    else:
        print("Not open")
        return False

def move_closed_files(path):
    """This function will take a path as input and will go down the tree listing all the files one by one and then call is_file_open() function to check if it is open.
    In case the file is not open, it will move the file to some desired path by calling move() function from source to a destination dir"""
    file_list = []
    for (root,dirs,files) in os.walk(path):
        for file_name in files:
            full_file_name = os.path.join(root, file_name)
            if not is_file_open(full_file_name): # Checking if the file is not open under if condition and if not open, move the file and if open skip and continue to the next file.
                file_list.append(full_file_name)
                print("File can be moved as not open ", file_name)
                source = full_file_name
                destdir = root.replace('fileStore','transferred')
                destination = source.replace('fileStore','transferred')
                if not os.path.exists(destdir):
                    os.makedirs(destdir)
                move(source,destination)
            else:
                continue

def move(src, dest):
    """This function is using shutil module to move source files to specified destination path"""
    shutil.move(src, dest)

# main function to start the process
move_closed_files(path)