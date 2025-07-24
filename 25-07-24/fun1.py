def plus(a, b): # 함수 정의 a -> 10, b -> 4
    result = a + b
    return result

a = plus(10, 4) # 함수 호출 14 -> a
print(a)

print(plus(10, 4))



def justPrint():
    print("안녕하세요")
    # return 없음, None이 출력되는 이유
justPrint()
print(justPrint())