import random
import sys
user_pass = input("패스워드를 입력하시오: ")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter1 in password:
    for letter2 in password:
        for letter3 in password:
            for letter4 in password:
                for letter5 in password:
                    # ... (중간 생략: 동일하게 for문 계속)
                    for letter45 in password:
                        guess = (
                            letter1 + letter2 + letter3 + letter4 + letter5
                            # ... (중간 생략: 나머지 letter6~letter45 추가)
                        )
                        if len(guess) > len(user_pass):
                            continue
                        print(guess)
                        if guess == user_pass:
                            print("당신의 패스워드는 " + guess)
                            sys.exit()