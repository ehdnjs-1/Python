# selenium2.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver=webdriver.Chrome()
#접속할 주소
driver.get("https://www.example.com")

#p 태그 요소만 접근하기
p_element=driver.find_element(By.TAG_NAME, 'p')
print("p 태그의 첫번째요소만 가져옴")
print(p_element) #p_element 변수에 담긴 p 태그 요소를 출력
#find_element는 p 태그의 첫번째요소만 가져옴

# print(type(p_element))
# print(p_element.text)

p_elements=driver.find_elements(By.TAG_NAME, 'p')
print(type(p_elements))
# find_elements는 파이썬의 리스트 형식 (모든 p태그 가져옴)

print("p 태그의 모든 요소 가져옴")
for p in p_elements:    #반복되는 'p' 요소의 텍스트 내용을 출력합니다
    print(p.text)