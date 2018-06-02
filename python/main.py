#Dépendances:
    #python3
    #docker


import sys, getopt
import os, fs
from datetime import date

import mineSgen as mSg

from coloration import bcolors
from Arbo import Arborescence

ADVANCED = False
QUIET = False

#Privilégier une baseSQLI afin de conserver plus facilement les donnée
# OU
# Créer un fichier mineSgen.conf qui contiendrait ces variables

options={
    'install_path':'/srv/',
    'dirName':'Minecraft',
    'prefer_minecraft_version':'last',
    'prefer_server_type':'bukkit',
    'language':'en'
}

app = Arborescence('/srv/'+options.get('dirName')+'/')

#Executer la génération de serveur dans le /tmp avant de tout copier dans le /srv et ensuite lancer le Serveur
#Ajouter la génération d'un web serveur permettant la gestions des divers fichier

    #if(not os.path.isdir(options.get('install_path'))):





def settings():
    print("Settings")


def mineSGen():
    print (bcolors.HEADER + "MineSGen" + bcolors.ENDC)
    print ("---------------------------\n")
    app.dirVerification()
    server = mSg.CreateServ()
    if ADVANCED:
      mSg.AdvancedSetServerProperties(server)
    else:
      mSg.StandardSetServerProperties(server)

    print(server.properties.get('server-name'))


def main(argv):
    os.system('clear')
    try:
        opts, args = getopt.getopt(argv,"haqs",["help","advanced","quiet","settings"])
    except getopt.GetoptError:
        print ('Nup\'')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
             print(bcolors.HEADER + 'mineSGen.py -   Minecraft Server Generator\n' + bcolors.ENDC)
             print('\t-a | --advanced : Lance l\'application en mode avancé')
             print('\t-q | --quiet :    Empêche l\'affichage des logs')
             print('\t-s |--settings :  Ouvre les settings')
             sys.exit()
        elif opt in ("-a", "--advanced"):
            ADVANCED = True
        elif opt in ("-q", "--quiet"):
            QUIET = True
        elif opt in ("-s","--settings"):
            settings()
            sys.exit()
    mineSGen()

if __name__ == "__main__":
   main(sys.argv[1:])
