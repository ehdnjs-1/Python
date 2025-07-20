dan = int(input("몇 단을 외울까요? (1~9): "))

for i in range(1, 10):
    answer = int(input(f"{dan} x {i} = ? "))
    if answer == dan * i:
        print("정답입니다!")
    else:
        print(f"틀렸어요. 정답은 {dan * i}입니다.")