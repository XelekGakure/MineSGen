#Dépendances:
    #python3
    #docker

import os, fs
from datetime import date


from coloration import bcolors
from Arbo import Arborescence

server={
    'properties':{
        'spawn-protection':16,
    	'max-tick-time':60000,
    	'server-name':'Unknown Server',
    	'generator-settings':'',
    	'force-gamemode':'false',
    	'allow-nether':'true',
    	'gamemode':0,
    	'enable-query':'false',
    	'player-idle-timeout':0,
    	'difficulty':1,
    	'spawn-monsters':'true',
    	'op-permission-level':4,
    	'resource-pack-hash':'',
    	'announce-player-achievements':'true',
    	'pvp':'true',
    	'snooper-enabled':'true',
    	'level-type':'DEFAULT',
    	'hardcore':'false',
    	'enable-command-block':'false',
    	'max-players':10,
    	'network-compression-threshold':256,
    	'max-world-size':29999984,
    	'server-port':25565,
    	'server-ip':'',
    	'spawn-npcs':'true',
    	'allow-flight':'false',
    	'level-name':'world',
    	'view-distance':12,
    	'resource-pack':'',
    	'spawn-animals':'true',
    	'white-list':'false',
    	'generate-structures':'true',
    	'online-mode':'false',
    	'max-build-height':256,
    	'level-seed':'',
    	'use-native-transport':'true',
    	'motd':'Baka No Laboratory',
    	'enable-rcon':'false'
    }
}

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


def log(log_data):
    print(str(date.today().year)+'-'+str(date.today().month))




def main():
    print (bcolors.HEADER + "Welcome in MineSgen" + bcolors.ENDC)
    print ("---------------------------\n")
    print(app.process_dir)

main()
