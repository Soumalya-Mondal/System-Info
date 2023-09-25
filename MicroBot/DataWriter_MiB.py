# ---------------- About ---------------- #
# Name --> DataWriter_MiB.py
# Description --> This module write data into file
# Developer --> Soumalya Mondal
# Prerequisite --> NameGenerator (Dev-Build), os (Python-inBuild)
# File Location --> ~/System-Info/MicroBot/DataWriter_MiB.py
# Callable Function --> 
# ---------------------------------------------------------------- #



# ---------------- Self Module Call Section ---------------- #
if __name__ == '__main__':
    # ---------------- Impoting Module ---------------- #
    from os import mkdir, getcwd
    from os.path import exists, join, dirname
    from NameGenerator_MiB import NameGenerator

    # ---------------- Define Class ---------------- #
    class DataWriter:
        # Initilize the class
        def __init__(self, data):
            self.data = data
            self.namegenerator = NameGenerator()
            self.datafolderdir = join(dirname(getcwd()), 'DataFolder')
            if not exists(self.datafolderdir):
                mkdir(self.datafolderdir)
                self.createfolder()
            else:
                self.createfolder()
        
        # To create folder
        def createfolder(self):
            self.foldername = self.namegenerator.foldername()
            self.folderdir = join(self.datafolderdir, self.foldername)
            if not exists(self.folderdir):
                mkdir(self.folderdir)
                self.filecreate()
            else:
                self.filecreate()
        
        # To create file
        def filecreate(self):
            self.filename = self.namegenerator.filename() + '.txt'
            self.filedir = join(self.folderdir, self.filename)
            self.writer()
        
        # To write data into file
        def writer(self):
            with open(self.filedir, 'w') as writer:
                for x, y in self.data.items():
                    writer.write(f'{x}: {y}\n')
            self.__repr__()
        
        # Return statement
        def __repr__(self):
            return f'Folder Name:{self.foldername}\nFolder Path:{self.folderdir}\nFile Name:{self.filename}\nFile Path:{self.filedir}'

    # ---------------- Debug Section ---------------- #
    sampledata = {'Developer':'Soumalya Mondal', 'Call By': 'DataWriter_MiB.py'}
    debug = DataWriter(data = sampledata)
    print('\n# ' + '-'*8 + ' Data Write Into File Information ' + '-'*8 + ' #\n')
    print(debug)
    print('\n# ' + '-'*48 + ' #\n')
# ---------------------------------------------------------------- #



# ---------------- Other Module Call Section ---------------- #
else:
    # ---------------- Impoting Module ---------------- #
    from os import mkdir, getcwd
    from os.path import exists, join
    from MicroBot.NameGenerator_MiB import NameGenerator

    # ---------------- Define Class ---------------- #
    class DataWriter:
        # Initialize class
        def __init__(self, data):
            self.data = data
            self.namegenerator = NameGenerator()
            self.datafolderdir = join(getcwd(), 'DataFolder')
            if not exists(self.datafolderdir):
                mkdir(self.datafolderdir)
                self.createfolder()
            else:
                self.createfolder()
        
        # To create folder
        def createfolder(self):
            self.foldername = self.namegenerator.foldername()
            self.folderdir = join(self.datafolderdir, self.foldername)
            if not exists(self.folderdir):
                mkdir(self.folderdir)
                self.filecreate()
            else:
                self.filecreate()
        
        # To create file
        def filecreate(self):
            self.filename = self.namegenerator.filename() + '.txt'
            self.filedir = join(self.folderdir, self.filename)
            self.writer()
        
        # To write data into file
        def writer(self):
            with open(self.filedir, 'w') as writer:
                for x, y in self.data.items():
                    writer.write(f'{x}: {y}\n')
            self.__repr__()
        
        # Return statement
        def __repr__(self):
            return f'Folder Name:{self.foldername}\nFolder Path:{self.folderdir}\nFile Name:{self.filename}\nFile Path:{self.filedir}'
# ---------------------------------------------------------------- #