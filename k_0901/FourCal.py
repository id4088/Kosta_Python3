class FourCal:

    result=0
    def __init__(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        FourCal.result =self.first+self.second
        return FourCal.result
    
    def minus(self):
        FourCal.result =self.first-self.second
        return FourCal.result
    
    def mul(self):
        FourCal.result =self.first*self.second
        return FourCal.result
    
    def div(self):
        FourCal.result =self.first/self.second
        return FourCal.result
           