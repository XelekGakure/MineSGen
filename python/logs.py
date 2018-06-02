from coloration import bcolors
from datetime import date

import os, fs, sys


def log(message,type):
    type = type.lower()
    if not QUIET:
        if type == 'error':
            print(bcolors.FAIL + "[" + bcolors.BOLD + " INFO " + bcolors.ENDC + bcolors.FAIL + "] - " + message + bcolors.ENDC)
        elif type == 'info':
            print(bcolors.HEADER + "[" + bcolors.CYAN + bcolors.BOLD + " INFO " + bcolors.ENDC + bcolors.HEADER + "] - " + message + bcolors.ENDC)
        elif type == 'success':
            print(bcolors.OKGREEN + "[" + bcolors.BOLD + " INFO " + bcolors.ENDC + bcolors.OKGREEN + "] - " + message + bcolors.ENDC)
    print('fichier de logs: ' + str(date.today().year)+'-'+str(date.today().month) + '.log')
