class Calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()



if __name__ =="__main__":
    print(cal1.add(3))
    print(cal2.add(4))
    print(cal1.add(3))
    print(cal2.add(7))
