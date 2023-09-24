# ---------------- About ---------------- #
# Name --> DataWriter_MiB.py
# Description --> This module write data into file
# Developer --> Soumalya Mondal
# Prerequisite --> NameGenerator (Dev-Build), os (Python-inBuild)
# File Location --> ~/System-Info/MicroBot/DataWriter_MiB.py
# Callable Function --> 
# ------------------------------------------------ #

# ---------------- Impoting Module ---------------- #
# Importing OS module
from os import mkdir, getcwd
from os.path import exists, join, dirname
# Importing NameGenerator_MiB module
from NameGenerator_MiB import NameGenerator
# ------------------------------------------------ #

# ---------------- Define Module Class ---------------- #
class DataWriter:

    # Initilize the class
    def __init__(self):
        # Create NameGenerator object
        self.folder = NameGenerator().foldername()
        self.file = NameGenerator().filename()
        # Make DataFolder path
        self.datafolderdir = join(dirname(getcwd()), 'DataFolder')
        # Check if DataFolder is exists or not
        if not exists(self.datafolderdir):
            # Create DataFolder directory
            mkdir(self.datafolderdir)
            # Call folder create function
            self.foldercreate(self, self.folder)
# ------------------------------------------------ #

# ---------------- Debug Section ---------------- #
# Calling main function
if __name__ == '__main__':

    # Define TimeInfo class object
    debug = DataWriter()

    # Printing all function output to check
    print('# ' + '-'*8 + ' System Current Date & Time Information ' + '-'*8 + ' #')
    # End line print
    print('# ' + '-'*48 + ' #')
# ------------------------------------------------ #