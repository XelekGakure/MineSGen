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

    def dirVerification():
        if(not os.path.isdir(options.get('install_path'))):
            os.mkdir(options.get('install_path'))
