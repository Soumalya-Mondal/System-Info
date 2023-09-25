# ---------------- About ---------------- #
# Name --> MasterBot.py
# Description --> This module create a System Information file
# Developer --> Soumalya Mondal
# Prerequisite --> TimeInfo_MiB (Dev-Build), NameGenerator_MiB (Dev-Build), DataWriter_MiB (Dev-Build)
# File Location --> ~/System-Info/MasterBot.py
# Callable Function -->
# ------------------------------------------------ #



# ---------------- Impoting Module ---------------- #
from MicroBot.TimeInfo_MiB import TimeInfo
from MicroBot.NameGenerator_MiB import NameGenerator
from MicroBot.DataWriter_MiB import DataWriter

# ---------------- Initial Main Function ---------------- #
if __name__ == '__main__':
    print('\n# ' + '-'*8 + ' MasterBot Information ' + '-'*8 + ' #')

    # Create TimeInfo objet
    timeinfo = TimeInfo()
    print(f'\nFrom TimeInfo Module\nDate:{timeinfo.date()}\nTime(12h):{timeinfo.time12h()}\nTime(24h):{timeinfo.time24h()}')

    # Create NameGenerator object
    namegenerator = NameGenerator()
    print(f'\nFrom NameGenerator Module\nFolder Name:{namegenerator.foldername()}\nFile Name:{namegenerator.filename()}')

    # Create DataWriter object
    sampledata = {'Date': timeinfo.date(), 'Time(12h)': timeinfo.time12h(), 'Time(24h)': timeinfo.time24h(), 'Developer': 'Soumalya Mondal'}
    datawriter = DataWriter(data = sampledata)
    print(f'\nFrom DataWriter Module\n{datawriter}')

    print('\n# ' + '-'*48 + ' #')
# ---------------------------------------------------------------- #