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
# ------------------------------------------------ #

# ---------------- Initial Main Function ---------------- #
if __name__ == '__main__':
    # Create TimeInfo objet
    timeinfo = TimeInfo()
    # Create NameGenerator object
    namegenerator = NameGenerator()

    # Print TimeInfo object
    print(f'\nFrom TimeInfo Module\nDate:{timeinfo.date()}\nTime(12h):{timeinfo.time12h()}\nTime(24h):{timeinfo.time24h()}')
    # Print NameGenerator object
    print(f'\nFrom NameGenerator Module\nFolder Name:{namegenerator.foldername()}\nFile Name:{namegenerator.filename()}')
# ------------------------------------------------ #