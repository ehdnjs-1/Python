# match.py
# 조건문 match_case
num = int(input("1~3숫자입력> "))
match num:
    case 1:
        print("1 입력")
    case 2:
        print("2 입력")
    case 3:
        print("3 입력")
    case _:
        print("1~3이외의 숫자")

