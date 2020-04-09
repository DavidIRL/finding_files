import os

def find_files(suffix, path):
    """ 
    Suffix should be file type as a string e.g. 'py' or 'txt'.
    \n path should be the name of the folder/directory as a string
    \n e.g. 'my_dir', 'New folder', 'FolderOfFolders', etc.
    \n path folder/directory should be in current working directory
    """
    if path not in os.listdir():
        return FileExistsError('Path not in current directory')
    elif not os.path.isdir(path):
        return FileExistsError('Path provided is not a folder/directory')
    return list_all(suffix, path)

def list_all(suffix, path):
    #all_files = []
    #folders = []
    layer = os.listdir(path)

    # of all the elements in the current 'layer' list add any files
    # ending in .'suffix' to 'all_files'
    all_files = [path + '/' + file for file in layer if '.' + suffix in file]
    # any elements that don't have '.' in name inferred as folder/dict
    folders = [folder for folder in layer if '.' not in folder]

    for folder in folders:
        # recurse through all_folders using list_all to extend the path
        # each recurse an updated path is made per folder depth
        all_files.extend(list_all(suffix= suffix, path=path + '/' + folder))
        # e.g.
        # path(root)/file1
        # root/subdir1/file2
        # root/subdir1/subdir2/file3
            
    return all_files


if __name__ == '__main__':
    print(find_files('h', 'subdir2')) # should return FileExistsError
    print(find_files('c', 'testdir')) # should return list of path lists for .c files'
    print(find_files('h', 'testdir')) # should return list of path lists for .c files'
    print(find_files('py', 'finding_files.py')) # should return FileExistsError