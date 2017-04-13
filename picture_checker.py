'''
Script to check folders full of pictures for duplicates
bad data &c. &c.
'''
FOLDER_PATH = "/media/tim/tims_data/tims_code/snippets/"
import os
import subprocess
import hashlib


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


def name_and_md5(fpaths):
    fpaths_out = []    
    for fpath in fpaths:
        fh = open(fpath['path'], 'r')
        hash = hashlib.md5(fh.read()).hexdigest()
        fpath2 = merge_two_dicts({'hash': hash}, fpath)      
        # print fpath2
        fpaths_out.append(fpath2)
    return fpaths_out


def main():
    walk = os.walk(FOLDER_PATH, topdown=True)
    fpaths = []
    for root, dirs, files in walk:
        for file in files:
            path = os.path.join(root, file)
            fpaths.append({"path": path,
                           "name": file})            
    #print fpaths    
    files = name_and_md5(fpaths)
    for file in files:
        for other_file in files:
            if file['hash'] == other_file['hash'] and file['path'] != other_file['path']:
                print "{} and \n{} \nare the same\n".format(file, other_file)
            


    
if __name__ == "__main__":
    main()
