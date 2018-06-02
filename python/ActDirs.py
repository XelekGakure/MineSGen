import os
import logs

def generateIfNotExist(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
        logs.log(str(dir) + " created" + bcolors.ENDC)

def LogIfExist(dir):
    if not os.path.isdir(dir):
        logs.log(str(dir) + " not exist" + bcolors.ENDC)
    else:
        logs.log(str(dir) + " exist" + bcolors.ENDC)
