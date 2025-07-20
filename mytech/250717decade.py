import sys
import itertools
import getpass

real_password = "dowon"  # 암호를 미리 지정

password = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(0, 10)]  # 알파벳+숫자

print("패스워드 분석 중...")  # 분석 시작 안내

found_password = None
for guess_tuple in itertools.product(password, repeat=len(real_password)):
    guess = ''.join(guess_tuple)
    print(f"암호해제 시도 중: {guess}")  # 현재 시도 중인 패스워드 출력
    if guess == real_password:
        found_password = guess
        break  # 찾은 값 저장 후 반복문 종료

max_attempts = 3
for attempt in range(max_attempts):
    user_input = getpass.getpass("암호를 입력하세요: ")
    if user_input == real_password:
        print("환영합니다 도원님")
        print(f"분석된 암호: {found_password}")  # 분석된 암호 보여주기
        break
    else:
        print("접근 거부")
        if attempt == max_attempts - 1:
            print("최대 시도 횟수를 초과했습니다. 프로그램을 종료합니다.")