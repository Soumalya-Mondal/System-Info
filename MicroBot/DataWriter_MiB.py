# ---------------- About ---------------- #
# Name --> DataWriter_MiB.py
# Description --> This module write data into file
# Developer --> Soumalya Mondal
# Prerequisite --> NameGenerator (Dev-Build), os (Python-inBuild)
# File Location --> ~/System-Info/MicroBot/DataWriter_MiB.py
# Callable Function --> 
# ------------------------------------------------ #

# ---------------- Impoting Module ---------------- #
# Importing os module
from os import mkdir, getcwd, rmdir
from os.path import exists, join, dirname
# Importing NameGenerator_MiB module
from MicroBot.NameGenerator_MiB import NameGenerator
# ------------------------------------------------ #

# ---------------- Define Module Class ---------------- #
class DataWriter:

    # Initilize the class
    def __init__(self, data):
        self.data = data
        # Create NameGenerator object
        self.namegenerator = NameGenerator()
        # Make DataFolder path
        self.datafolderdir = join(getcwd(), 'DataFolder')
        # Check if DataFolder is exists or not
        if not exists(self.datafolderdir):
            # Create DataFolder directory
            mkdir(self.datafolderdir)
            # Call createfolder function to create folder
            self.createfolder()
        else:
            # Call createfolder function to create folder
            self.createfolder()
    
    # To create folder
    def createfolder(self):
        # Get folder name
        self.foldername = self.namegenerator.foldername()
        # Make folder directory
        self.folderdir = join(self.datafolderdir, self.foldername)
        # Check if the directory is present or not
        if not exists(self.folderdir):
            # Create sub directory if not present
            mkdir(self.folderdir)
            # Call filecreate function to create file
            self.filecreate()
        else:
            # Call filecreate function to create file
            self.filecreate()
    
    # To create file
    def filecreate(self):
        # Get file name
        self.filename = self.namegenerator.filename() + '.txt'
        # Make file directory
        self.filedir = join(self.folderdir, self.filename)
        # Call writer function to write data into file
        self.writer()
    
    # To write data into file
    def writer(self):
        # Create file
        with open(self.filedir, 'w') as writer:
            # Extract data from data dict
            for x, y in self.data.items():
                # Write into file
                writer.write(f'{x}: {y}\n')
        # Call return print function
        self.__repr__()
    
    # To return Success statement
    def __repr__(self):
        return f'Folder Path:{self.folderdir}\nFile Path:{self.filedir}'
# ------------------------------------------------ #

# ---------------- Debug Section ---------------- #
# Calling main function
if __name__ == '__main__':

    # Define TimeInfo class object
    debug = DataWriter()

    # Printing all function output to check
    print('# ' + '-'*8 + ' Data Write Into File Information ' + '-'*8 + ' #')
    # End line print
    print('# ' + '-'*48 + ' #')
# ------------------------------------------------ #