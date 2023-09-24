# Description --> This module create various time information
# Developer --> Soumalya Mondal
# Prerequisite --> datetime (Python-inbuild)
# File Location --> ~/System-Info/MicroBot/TimeInfo_MiB.py
# Callable Function --> date(), time12h(), time24h()

# ---------------- Impoting Module ---------------- #
# Importing datetime module
from datetime import datetime as dt
# ------------------------------------------------ #

# ---------------- Define Module Class ---------------- #
class TimeInfo:

    # Initilize the class
    def __init__(self):
        self.dtNow = dt.now()

    # Create today's date fucntion
    def date(self):
        date = self.dtNow.strftime('%d-%b-%Y')
        return date
    
    # Create current time(12H) function
    def time12h(self):
        time = self.dtNow.strftime('%I:%M:%S.%f %p')
        return time
    
    # Create current time(24H) function
    def time24h(self):
        time = self.dtNow.strftime('%H:%M:%S.%f')
        return time
# ------------------------------------------------ #

# ---------------- Debug Section ---------------- #
# Calling main function
if __name__ == '__main__':

    # Define TimeInfo class object
    debug = TimeInfo()

    # Printing all function output to check
    print('# ' + '-'*8 + ' System Current Date & Time Information ' + '-'*8 + ' #')

    # Print today's date
    print(f'\tCurret Date: {debug.date()}')
    # Print current time(12H)
    print(f'\tCurrent Time(12H): {debug.time12h()}')
    # Print current time(24H)
    print(f'\tCurrent Time(24H): {debug.time24h()}')
    # End line print
    print('# ' + '-'*48 + ' #')
# ------------------------------------------------ #