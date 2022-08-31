## Q2
i=1000

def Quize2(number):
    total=0
    j=0
    while j<=number:
        if j%3 ==0:
            total +=j
            j+=1
        else:
            j+=1
    print(total)


##Q3

k=5

def Imaging(n):
    i=1
    
    while i<=n:
        print("*"*i)
        i+=1

## Q4 for 반복문

Q4=100

def Printing(number):
    numbering = range(1,number+1)
    for i in numbering:
        print(i)
        
## Q5 for문 평균점수 구하기

Q5 =[70,60,55,75,95,90,80,80,85,100]

def Avg_score(People_score):
    total =0
    Person=0
    for score in People_score:
        total+=int(score)
        Person+=1
    print(total/Person)

## Q6 리스트 내포

numbers = [1,2,3,4,5]
result = [i*2 for i in numbers if i%2 ==1 ]


if __name__ =="__main__":
    Quize2(i)
    Imaging(k)
    Printing(Q4)
    Avg_score(Q5)
    print(result)