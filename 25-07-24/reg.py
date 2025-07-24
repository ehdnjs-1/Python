import re
#정규 표현식 모듈을 불러옵니다. Regualr Expression은 문자열에서 특정 패턴을 찾거나 대체하는 데 사용됩니다.

pattern = r'^[\w-]+@[\w-]+\.[a-zA-Z]{2,4}$'

def check_email(email):
    if re.match(pattern, email):
        print(f"'{email}'은 유효한 이메일 주소입니다.")
    else:
        print(f"'{email}'은 유효하지 않은 이메일 주소입니다.")

email = input("이메일 주소를 입력하세요: ")
check_email(email)


# pattern = r'010-\d\d\d\d-\d\d\d\d'
# found=re.search(pattern, '제 휴대폰 번호는 010-1234-5678입니다.')
# #일치하는 부분을 처음부터 끝까지 탐색
# print('발견된 휴대폰 번호: ' + found.group())
# #찾아서 일치한 문자열 전체를 반환