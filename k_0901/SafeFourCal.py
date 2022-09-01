from FourCal import *

class SafeFourCal(FourCal):
    
    def divide(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
