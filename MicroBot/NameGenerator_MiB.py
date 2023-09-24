# ---------------- About ---------------- #
# Name --> NameGenerator_MiB.py
# Description --> This module create file and folder name
# Developer --> Soumalya Mondal
# Prerequisite --> datetime (Python-inBuild)
# File Location --> ~/System-Info/MicroBot/NameGenerator_MiB.py
# Callable Function --> foldername(), filename()
# ------------------------------------------------ #

# ---------------- Impoting Module ---------------- #
# Importing datetime module
from datetime import datetime as dt
# ------------------------------------------------ #

# ---------------- Define Module Class ---------------- #
class NameGenerator:
    
    # Initilize the class
    def __init__(self):
        self.dtNow = dt.now()

    # Create folder name function
    def foldername(self):
        foldername = self.dtNow.strftime('%d-%B-%Y')
        return foldername
    
    # Create file name function
    def filename(self):
        filename = self.dtNow.strftime('%Hh-%Mm-%Ss-%fms')
        return filename
# ------------------------------------------------ #

# ---------------- Debug Section ---------------- #
# Calling main function
if __name__ == '__main__':

    # Define NameGenerator class object
    debug = NameGenerator()

    # Printing all function output to check
    print('# ' + '-'*8 + ' Folder & File Name Generator ' + '-'*8 + ' #')
    # Print folder name
    print(f'\tFolder Name: {debug.foldername()}')
    # Print file name
    print(f'\tFile Name: {debug.filename()}')
    # End line print
    print('# ' + '-'*48 + ' #')
# ------------------------------------------------ #