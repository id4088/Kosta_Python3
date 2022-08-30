## Q1 홍길동 평균정수 구하기

Hong_score={'국어':80,'영어':75,'수학':55}


def Average_Score(People_score):
    total=0
    subject_count=0
    for subject in People_score:
        total += People_score[subject]
        subject_count+=1
    avg=total/subject_count
    print(avg)


## Q2 홀수 짝수 판별기

Number=13

def Odd_or_Even(int):
    if Number%2 == 0:
        print("짝수 입니다")
    elif Number%2 == 1:
        print("홀수 입니다")

## Q3 슬라이싱

People_info = "881120-1068234"

def Info_Check(Person):
    Num = Person[:6]
    Birth = Person[7:]
    print("주민 등록 번호",":",Num)
    print("생년월일",":",Birth)

## 주민 등록 번호 성별 출력 문자열 인덱싱

def People_Sex(Person):
    Sex=Person[7]
    if (Sex=='1'):
        print("남자입니다")
    elif (Sex=='0'):
        print("여자입니다")
    else:
        print("인간이 아닙니다")

        
if __name__=="__main__":
    Average_Score(Hong_score)
    Odd_or_Even(Number)
    Info_Check(People_info)
    People_Sex(People_info)