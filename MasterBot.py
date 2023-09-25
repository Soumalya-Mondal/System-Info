# ---------------- About ---------------- #
# Name --> MasterBot.py
# Description --> This module create a System Information file
# Developer --> Soumalya Mondal
# Prerequisite --> TimeInfo_MiB (Dev-Build)
# File Location --> ~/System-Info/MasterBot.py
# Callable Function -->
# ------------------------------------------------ #

# ---------------- Impoting Module ---------------- #
# Importing TimeInfo_MiB module
from MicroBot.TimeInfo_MiB import TimeInfo
# Importing NameGenerator_MiB module
from MicroBot.NameGenerator_MiB import NameGenerator
# Importing DataWriter_MiB module
from MicroBot.DataWriter_MiB import DataWriter
# ------------------------------------------------ #

# ---------------- Initial Main Function ---------------- #
if __name__ == '__main__':
    # Printing all function output to check
    print('\n# ' + '-'*8 + ' MasterBot Information ' + '-'*8 + ' #')

    # Create TimeInfo objet
    timeinfo = TimeInfo()
    # Print TimeInfo object
    print(f'\nFrom TimeInfo Module\nDate:{timeinfo.date()}\nTime(12h):{timeinfo.time12h()}\nTime(24h):{timeinfo.time24h()}')

    # Create NameGenerator object
    namegenerator = NameGenerator()
    # Print NameGenerator object
    print(f'\nFrom NameGenerator Module\nFolder Name:{namegenerator.foldername()}\nFile Name:{namegenerator.filename()}')

    # Sample data for testing
    sampledata = {'Date': timeinfo.date(), 'Time(12h)': timeinfo.time12h(), 'Time(24h)': timeinfo.time24h(), 'Developer': 'Soumalya Mondal'}
    # Create DataWriter object
    datawriter = DataWriter(data = sampledata)
    # Print return statement
    print(f'\nFrom DataWriter Module\n{datawriter}')

    # End line print
    print('\n# ' + '-'*48 + ' #')
# ------------------------------------------------ #