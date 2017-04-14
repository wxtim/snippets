'''
Script to check folders full of pictures for duplicates
bad data &c. &c.
'''
import os
import hashlib
import collections
import sys

EXTENSIONS = ['.jpg', '.jpeg', '.png']
try:
    _, FOLDER_PATH = sys.argv
except:
    msg = "This programme requires a folder path as a command line argument"
    raise TypeError(msg)

def merge_two_dicts(dictx, dicty):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    dictz = dictx.copy()
    dictz.update(dicty)
    return dictz


def name_and_md5(fpaths):
    """
    Takes a dictionary of form ({"path": path,
                           "name": file})
    and returns an additional keypair
    'hash' which is an MD5 checksum of the
    content of the file
    """
    fpaths_out = []
    for fpath in fpaths:
        fhandle = open(fpath['path'], 'r')
        hash_ = hashlib.md5(fhandle.read()).hexdigest()
        fpath2 = merge_two_dicts({'hash': hash_}, fpath)
        # print fpath2
        fpaths_out.append(fpath2)
    return fpaths_out


def main():
    """
    The main programme. This is designed to take a
    list of folders and return cases where files within those
    folders have duplicate content.
    @todo: probably needs refactoring because it is a bit of a
    mess
    """
    walk = os.walk(FOLDER_PATH, topdown=True)
    fpaths = []
    for root, _, files in walk:
        for file_ in files:
            path = os.path.join(root, file_)
            fpaths.append({"path": path,
                           "name": file_})

    files = name_and_md5(fpaths)
    count = collections.Counter()
    for file_ in files:
        count[file_['hash']] += 1

    ls_duplicate_hashes = []
    for key, value in count.iteritems():
        if value > 1:
            ls_duplicate_hashes.append(key)

    dup_hashes = []
    for hash_ in ls_duplicate_hashes:
        dup_hash = []
        for file_ in files:
            if file_['hash'] == hash_:
                dup_hash.append(file_)
        if len(dup_hash) != 0:
            dup_hashes.append(dup_hash)

    output_file = open('output.txt', 'w')
    for hash_ in dup_hashes:
        hash2 = hash_[0]['hash']
        output_file.writelines("\nThe following files all have the same MD5 Hash: {}\n".format(hash2))
        for files in hash_:
            
            output_file.writelines("{}\n".format(str(files)))



if __name__ == "__main__":
    main()
