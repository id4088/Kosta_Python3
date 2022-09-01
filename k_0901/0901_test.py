## Q1 홀 짝 판별 함수

Q1_ex=11

def is_odd(number):
    if number%2==0:
        print("짝수 입니다.")
    elif number%2==1:
        print("홀수 입니다.")

## 입력으로 들어 오는 모든 수의 평균 값을 계산하는 함수

#
#def Avg():
#    i=0
#    total = 0
#    while i !="":
#        try: 
#            number= int(input("숫자를 입력하세요 : "))
#            total += number
#            i+=1
#        except IndentationError as e:
#            print(e)
#            break
#    print(number/len(number))




if __name__ == "__main__":
    is_odd(Q1_ex)
    
    