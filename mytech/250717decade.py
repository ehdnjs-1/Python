import sys
import itertools
import getpass

user_pass = getpass.getpass("패스워드를 입력하시오: ")  # 화면에 표시되지 않음
password = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(0, 10)]  # 알파벳+숫자

for guess_tuple in itertools.product(password, repeat=len(user_pass)):
    guess = ''.join(guess_tuple)
    if guess == user_pass:
        break  # 반복문만 종료

# 아래에 보안 프로그램 코드 추가 (최대 3번 시도)
real_password = user_pass  # 위에서 입력받은 패스워드를 실제 암호로 사용

max_attempts = 3
for attempt in range(max_attempts):
    user_input = getpass.getpass("암호를 입력하세요: ")
    if user_input == real_password:
        print("접근 허가")
        break
    else:
        print("접근 거부")
        if attempt == max_attempts - 1:
            print("최대 시도 횟수를 초과했습니다. 프로그램을 종료합니다.")