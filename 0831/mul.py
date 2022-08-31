main=range(2,10)
sub=range(1,10)
def gugudan():
    for i in main:
        for j in sub:
            result = i*j
            print("%d x %d : %d"%(i,j,result))

if __name__ =='__main__':
    print(__name__)