import sys

if len(sys.argv)!=3:
    print("인자는 2개의 숫자입니다")
    sys.exit()
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(sys.argv[0],sys.argv[1],sys.argv[2])
