password =""

while password != "dowon":
    password = input("암호를 입력하시오:")
    print("로그인 성공")


cnt = 0
sum = 0
while cnt <=100:
    sum=sum+cnt
    cnt=cnt+1
print("합계=",sum)

# 정수를 반복적으로 입력받다가
# 짝수가 5개 입력되면 반복문을 종료하시오.
i= 0
while i<5 :
    num= int(input("정수입력> "))
    if num % 2 == 0:
        i=i+1
print("반복문 종료")
