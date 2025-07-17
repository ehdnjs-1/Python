for i in range (5, 0,-1):
    for j in range(0,1):
        print("*", end="")
    print()




fruit = ['참외', '파인애플', '사과', '바나나', '골드키위', '배']
cart = [] #빈 리스트 선언
for k in fruit:
    if len(k) >=3:
        cart.append(k)
print(cart)
#-----------------
과자 = {
"꼬깔콘": 2000,
"새우깡": 3830,
"포카칩": 1180
}
for k,v in 과자.items():
    print(k,v)
