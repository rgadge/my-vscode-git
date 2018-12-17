import os
import subprocess

path = '/Users/rajneeshgadge/.vscode/'

def tree_print(root):
    for root, dirs, files in os.walk(root):
        for f in files:
            filename = (os.path.join(root, f))
            bashCommand = "echo " + filename
            output = os.system(bashCommand)


def is_file_open(file_name):
    print "Checking ", file_name, " - ",
    process = subprocess.Popen(["lsof", file_name], stdout=subprocess.PIPE)
    process.communicate()[0]
    if process.returncode == 0:
        print "Open!"
        return True
    else:
        print "Not open"
        return False


def get_open_files(source):
    file_list = []
    for (root,dirs,files) in os.walk(source):
        for file_name in files:
            full_file_name = os.path.join(root, file_name)
            if (is_file_open(full_file_name)):
                file_list.append(full_file_name)
    return file_list

tree_print(path)
