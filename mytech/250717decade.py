import sys
import itertools
import getpass
import random
import string
import time

# 금고 발견 상황 연출
print("당신은 금고를 발견했습니다.")
print("금고를 열기 위해 암호해제를 진행하시겠습니까? (예/아니오)")
answer = input("답변: ")

if answer.strip() != "예" or answer.strip() != "응":
    print("암호해제를 중단합니다.")
    sys.exit()

# 1. 랜덤 비밀코드 생성 (금고 비밀번호)
secret_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

password = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(0, 10)]  # 알파벳+숫자

print("패스워드 분석 중... (6초간 시도)")

start_time = time.time()
found_code = None
for guess_tuple in itertools.product(password, repeat=len(secret_code)):
    guess = ''.join(guess_tuple)
    print(f"패스워드 분석중: {guess}")
    if guess == secret_code:
        found_code = guess
        break
    # 6초가 지나면 중단
    if time.time() - start_time > 8:
        print("패스워드 분석완료!")
        break

# 2. 암호 확인 코드 입력
max_attempts = 3
for attempt in range(max_attempts):
    user_input = getpass.getpass(f"암호를 확인하기 위한 코드를 입력하세요 (시도 {attempt + 1}/{max_attempts}): ")
    if user_input == "dowon":
        print("암호가 일치합니다. ")
        break
    else:
        print("접근 거부.")
        if attempt < max_attempts - 1:
            print("다시 시도하세요.")
