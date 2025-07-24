# 2~9단 출력

con=True
while con : #True(1)->무한 반복

 def gugu1():
    for i in range(2, 10): #2~9단
        for j in range(1, 10): #1~9
            print(f"{i} * {j} = {i*j}")
        print(i, "*", j, "=", i*j) #단이 끝나면 줄바꿈

def gugu2():
    for i in range(2, 10): #2~9단
        for j in range(1, 10): #1~9
            print(f"{i} * {j} = {i*j}", end="\t") #end="\t"로 탭 간격으로 출력
        print(i, "*", j, "=", i*j, end="  ") #단이 끝나면 줄바꿈


    num=int(input("메뉴를 입력하세요(1은 세로형 구구단, 2는 가로형 구구단, 0 종료)"))
    if num == 1 :
        print("1선택-세로형 구구단")
        gugu1()  #함수 호출

    elif num == 2 :
        print("2선택-세로형 구구단")
        gugu2()
        
    elif num == 0 :
        print("종료")
        con = False
    else :
        print("메뉴 선택 오류, 다시 입력하세요")
        