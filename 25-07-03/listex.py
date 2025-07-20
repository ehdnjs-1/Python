# 숫자를 3개를 input으로 입력
# 숫자는 list로 구성(0~2번째 방에 저장)
# 총점, 평균 구하여 출력
score=[0,0,0]
score.append(int(input("수학점수 :")))
score.append(int(input("영어점수 :")))
score.append(int(input("국어점수 :")))
# tot = score[0]+score[1]+score[2]
tot = sum(score)
avg = round(tot / 3,2)  # round는 반올림   # 정수와 정수 ---> 실수 나올수도 있음.
print("총점은" , tot, "평균은" , avg)
