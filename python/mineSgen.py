import os, fs, sys
import logs

from coloration import bcolors

class minecraftServer:
    def __init__(self):
        self.properties={
                'spawn-protection':16,
            	'max-tick-time':60000,
            	'server-name':'Unknown Server',                #
            	'generator-settings':'',
            	'force-gamemode':'false',                      #
            	'allow-nether':'true',                         #
            	'gamemode':0,                                  #
            	'enable-query':'false',
            	'player-idle-timeout':0,
            	'difficulty':1,                                #
            	'spawn-monsters':'true',                       #
            	'op-permission-level':4,
            	'resource-pack-hash':'',
            	'announce-player-achievements':'true',         #
            	'pvp':'true',                                  #
            	'snooper-enabled':'true',
            	'level-type':'DEFAULT',                        #
            	'hardcore':'false',                            #
            	'enable-command-block':'false',                #
            	'max-players':10,                              #
            	'network-compression-threshold':256,
            	'max-world-size':29999984,
            	'server-port':25565,
            	'server-ip':'',
            	'spawn-npcs':'true',                           #
            	'allow-flight':'false',                        #
            	'level-name':'world',
            	'view-distance':12,                            #
            	'resource-pack':'',
            	'spawn-animals':'true',                        #
            	'white-list':'false',                          #
            	'generate-structures':'true',                  #
            	'online-mode':'false',                         #
            	'max-build-height':256,
            	'level-seed':'',                               #
            	'use-native-transport':'true',
            	'motd':'Baka No Laboratory',                   #
            	'enable-rcon':'false'
            }

    def changeProperty(self, property, regex):
        while True:
            try:
                propertyModif = input(str(property) + ' [' + str(self.properties.get(property)) + '] :').strip()
                if propertyModif in [str(self.properties.get(property)), '']:
                    propertyModif = str(self.properties.get(property))
                else:
                    self.properties[property] = propertyModif

            except:
                print("Merci de respecter la convention de caractère")
            break


def CreateServ():
    return minecraftServer()

regex='a'

def StandardSetServerProperties(server):


    #Name
    server.changeProperty('server-name', regex)
    #Gamemode
    server.changeProperty('gamemode', regex)
    server.changeProperty('force-gamemode', regex)
    #Map
    server.changeProperty('allow-nether', regex)
    server.changeProperty('level-type', regex)
    server.changeProperty('generate-structures', regex)
    server.changeProperty('level-seed', regex)
    #Player
    server.changeProperty('difficulty', regex)
    server.changeProperty('hardcore', regex)
    server.changeProperty('pvp', regex)
    #Spawning
    server.changeProperty('spawn-monsters', regex)
    server.changeProperty('spawn-npcs', regex)
    server.changeProperty('spawn-animals', regex)
    #Administration
    server.changeProperty('enable-command-block', regex)
    server.changeProperty('max-players', regex)
    server.changeProperty('allow-flight', regex)
    server.changeProperty('view-distance', regex)
    server.changeProperty('white-list', regex)
    #Chatbox
    server.changeProperty('announce-player-achievements', regex)
    #Derniers Demandés:
    server.changeProperty('online-mode', regex)
    server.changeProperty('motd', regex)


def AdvancedSetServerProperties(server):
    #Name
    server.changeProperty('server-name', regex)
    #Gamemode
    server.changeProperty('gamemode', regex)
    server.changeProperty('force-gamemode', regex)
    #Map
    server.changeProperty('allow-nether', regex)
    server.changeProperty('level-type', regex)
    server.changeProperty('generate-structures', regex)
    server.changeProperty('level-seed', regex)
    #Player
    server.changeProperty('difficulty', regex)
    server.changeProperty('hardcore', regex)
    server.changeProperty('pvp', regex)
    #Spawning
    server.changeProperty('spawn-monsters', regex)
    server.changeProperty('spawn-npcs', regex)
    server.changeProperty('spawn-animals', regex)
    #Administration
    server.changeProperty('enable-command-block', regex)
    server.changeProperty('max-players', regex)
    server.changeProperty('allow-flight', regex)
    server.changeProperty('view-distance', regex)
    server.changeProperty('white-list', regex)
    #Chatbox
    server.changeProperty('announce-player-achievements', regex)
    #AdvancedTools
    server.changeProperty('spawn-protection', regex)
    server.changeProperty('max-tick-time', regex)
    server.changeProperty('generator-settings', regex)
    server.changeProperty('enable-query', regex)
    server.changeProperty('player-idle-timeout', regex)
    server.changeProperty('snooper-enabled', regex)
    server.changeProperty('network-compression-threshold', regex)
    server.changeProperty('max-world-size', regex)
    server.changeProperty('level-name', regex)
    server.changeProperty('use-native-transport', regex)
    server.changeProperty('enable-rcon', regex)
    server.changeProperty('max-build-height', regex)
    server.changeProperty('resource-pack-hash', regex)
    server.changeProperty('resource-pack', regex)
    server.changeProperty('op-permission-level', regex)
    #Derniers Demandés:
    server.changeProperty('online-mode', regex)
    server.changeProperty('motd', regex)
