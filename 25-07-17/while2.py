#while2.py
total=0
answer='yes'

while answer == 'yes':
    num=int(input("숫자를 입력하세요: "))
    total = total + num
    answer=input("계속 진행하시겠습니까?(yes/no)")
print("합계는:", total)
