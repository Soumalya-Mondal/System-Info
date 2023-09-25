# ---------------- About ---------------- #
# Name --> NameGenerator_MiB.py
# Description --> This module create file and folder name
# Developer --> Soumalya Mondal
# Prerequisite --> datetime (Python-inBuild)
# File Location --> ~/System-Info/MicroBot/NameGenerator_MiB.py
# Callable Function --> foldername(), filename()
# ------------------------------------------------ #



# ---------------- Self Module Call Section ---------------- #
if __name__ == '__main__':
    # ---------------- Impoting Module ---------------- #
    from datetime import datetime as dt

    # ---------------- Define Class ---------------- #
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
        
    # ---------------- Debug Section ---------------- #
    debug = NameGenerator()
    print('\n# ' + '-'*8 + ' Folder & File Name Generator ' + '-'*8 + ' #\n')
    print(f'Folder Name: {debug.foldername()}')
    print(f'File Name: {debug.filename()}.txt')
    print('\n# ' + '-'*48 + ' #\n')
# ---------------------------------------------------------------- #



# ---------------- Other Module Call Section ---------------- #
else:
    # ---------------- Impoting Module ---------------- #
    from datetime import datetime as dt

    # ---------------- Define Class ---------------- #
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
# ---------------------------------------------------------------- #