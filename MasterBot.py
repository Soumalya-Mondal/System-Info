# Description --> This module create a System Information file
# Developer --> Soumalya Mondal
# Prerequisite --> TimeInfo_MiB (Dev-Build)
# File Location --> ~/System-Info/MasterBot.py
# Callable Function -->

# ---------------- Impoting Module ---------------- #
# Importing TimeInfo_MiB module
from MicroBot.TimeInfo_MiB import TimeInfo
# ------------------------------------------------ #

# ---------------- Initial Main Function ---------------- #
if __name__ == '__main__':
    # Create TimeInfo objet
    timeinfo = TimeInfo()

    # Print TimeInfo object
    print(f'Date:{timeinfo.date()} Time(12h):{timeinfo.time12h()} Time(24h):{timeinfo.time24h()}')
# ------------------------------------------------ #