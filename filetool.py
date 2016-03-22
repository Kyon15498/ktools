import os
import shutil

def folderMerge(rootFolder = "./", newDir = './', mode = 'move', deleteSubdir = False):
    '''
    used to merge some folders,put files in them into $newDir
    deleteSubdir may have permission error   
    '''
    dirs = filter(os.path.isdir, os.listdir(rootFolder))
    func = {"move": shutil.move,"copy":shutil.copyfile}[mode]
    for d in dirs:
        files = os.listdir(os.path.join(rootFolder, d))
        for f in files:
            func(os.path.join(rootFolder,d,f), os.path.join(newDir,f))

    if deleteSubdir:
        import stat
        for d in dirs:
            os.chmod( filename, stat.S_IWRITE )
            os.rmdir(os.path.join(rootFolder,d))