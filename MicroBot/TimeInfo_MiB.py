# ---------------- About ---------------- #
# Name --> TimeInfo_MiB.py
# Description --> This module create various date & time information
# Developer --> Soumalya Mondal
# Prerequisite --> datetime (Python-inBuild)
# File Location --> ~/System-Info/MicroBot/TimeInfo_MiB.py
# Callable Function --> date(), time12h(), time24h()
# ------------------------------------------------ #



# ---------------- Self Module Call Section ---------------- #
# Calling main function
if __name__ == '__main__':
    # ---------------- Impoting Module ---------------- #
    from datetime import datetime as dt

    # ---------------- Define Class ---------------- #
    class TimeInfo:
        # Initilize the class
        def __init__(self):
            self.dtNow = dt.now()

        # Create date fucntion
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

    # Define TimeInfo class object
    debug = TimeInfo()
    print('\n# ' + '-'*8 + ' System Current Date & Time Information ' + '-'*8 + ' #\n')
    print(f'Curret Date: {debug.date()}')
    print(f'Current Time(12H): {debug.time12h()}')
    print(f'Current Time(24H): {debug.time24h()}')
    print('\n# ' + '-'*48 + ' #\n')
# ---------------------------------------------------------------- #



# ---------------- Other Module Call Section ---------------- #
else:
    # ---------------- Impoting Module ---------------- #
    from datetime import datetime as dt

    # ---------------- Define Class ---------------- #
    class TimeInfo:
        # Initilize the class
        def __init__(self):
            self.dtNow = dt.now()

        # Create date fucntion
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
# ---------------------------------------------------------------- #