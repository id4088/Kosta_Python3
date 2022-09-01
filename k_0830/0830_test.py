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

## Q4 주민 등록 번호 성별 출력 문자열 인덱싱

def People_Sex(Person):
    Sex=Person[7]
    if (Sex=='1'):
        print("남자입니다")
    elif (Sex=='0'):
        print("여자입니다")
    else:
        print("인간이 아닙니다")

## Q5 문자열 replace

Example = "a:b:c:d"

def Replace(Sentance):
    Sentance_=Sentance.replace(":","#")
    print(Sentance_)

##Q6 리스트 교체

list_ex = [1,3,5,4,2]

def List_Ch(list_ex):
    list_ex.sort()
    list_ex.reverse()
    print(list_ex)

##Q7 리스트를 문자열로

famous_saying = ['Life','is','too','short']

def Make_String(list_ex):
    List_ex=" ".join(list_ex)
    print(List_ex)

##Q8 튜블에 값 추가하기

tuple_ex1=(1,2,3)

def tuple_Add(tuple_ex):
    tuple_add=(4,)
    tuple_result=tuple_ex + tuple_add
    print(tuple_result)

## Q10 딕셔너리값 추출

dic_ex1={'A':90,'B':80,'C':70}

def dic_extract(dic_ex):
    dic_ex.pop('B')
    print(dic_ex)


## Q11 중복 숫자 제거

list_ex2 = [1,1,1,2,2,3,3,3,4,5]

def List_set(list_ex):
    list_set=list(set(list_ex))
    print(list_set)


if __name__=="__main__":
    Average_Score(Hong_score)
    Odd_or_Even(Number)
    Info_Check(People_info)
    People_Sex(People_info)
    Replace(Example)
    List_Ch(list_ex)
    Make_String(famous_saying)
    tuple_Add(tuple_ex1)
    dic_extract(dic_ex1)
    List_set(list_ex2)
