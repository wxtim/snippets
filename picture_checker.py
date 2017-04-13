'''
Script to check folders full of pictures for duplicates
bad data &c. &c.
'''
FOLDER_PATH = "/media/tim/tims_data/tims_code/snippets/"
EXTENSIONS =['.jpg', '.jpeg', '.png']
import os
import subprocess
import hashlib
import collections

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

    files = name_and_md5(fpaths)
    count = collections.Counter()
    for f in files:
        count[f['hash']] +=1

    ls_duplicate_hashes = []
    for key, value in count.iteritems():
        if value > 1:
            ls_duplicate_hashes.append(key)


    dup_hashes = []
    for hash in ls_duplicate_hashes:
        dup_hash = []
        for f in files:           
            if f['hash'] == hash:
                dup_hash.append(f)

        
        if len(dup_hash) != 0:
            dup_hashes.append(dup_hash)


    for hash in dup_hashes:
        h =  hash[0]['hash'] 
        print "The following files all have the same MD5 Hash:  ", h
        for files in hash:
            # for file in files.items():
            print files
            
   


    
if __name__ == "__main__":
    main()
