import sys
import itertools
import getpass
import random
import string
import time

# 1. 랜덤 비밀코드 생성 (예: 6자리)
secret_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

password = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(0, 10)]  # 알파벳+숫자

print("패스워드 분석 중... (6초간 시도)")

start_time = time.time()
found_code = None
for guess_tuple in itertools.product(password, repeat=len(secret_code)):
    guess = ''.join(guess_tuple)
    print(f"암호해제 시도 중: {guess}")
    if guess == secret_code:
        found_code = guess
        break
    # 6초가 지나면 중단
    if time.time() - start_time > 6:
        print("암호해제 시도 종료!")
        break

# 2. 암호 확인 코드 입력
user_input = getpass.getpass("암호를 확인하기 위한 코드를 입력하세요: ")
if user_input == "dowon":
    print(f"내가 생각한 비밀코드는: {secret_code}")
else:
    print("접근 거부")