import os, fs

import ActDirs

class Arborescence:
    def __init__(self, root_dir):
        self.root_dir=str(root_dir)

        #process
        self.process_dir=str(root_dir+'process/')
        #process/sources
        self.sources_dir=str(root_dir+'process/sources/')
        self.addons_sources_dir=str(root_dir+'process/sources/addons/')
        #process/sources/
        self.server_sources_dir=str(root_dir+'process/sources/Server/')
        #process/backendProcesses
        self.backend_process_dir=str(root_dir+'process/backendProcesses/')

        #Launch
        self.launch_dir=str(root_dir+'Launch/')

        #Servers
        self.servers_dir=str(root_dir+'Servers/')


    def dirVerification(self):
        ActDirs.generateIfNotExist(self.root_dir)
        ActDirs.generateIfNotExist(self.process_dir)
        ActDirs.generateIfNotExist(self.sources_dir)
        ActDirs.generateIfNotExist(self.addons_sources_dir)
        ActDirs.generateIfNotExist(self.backend_process_dir)
        ActDirs.generateIfNotExist(self.launch_dir)
        ActDirs.generateIfNotExist(self.servers_dir)
