score=int(input("점수를 입력하시오.: "))

if score>80:
    print("학점은 A입니다.")
elif score>60:
    print("학점은 B입니다.")
elif score>40:
    print("학점은 C입니다.")
elif score>20:
    print("학점은 D입니다.")
else:
    print("학점은 E입니다.")
    
# if score < 101 and score > 80:
#     print("학점A")
# elif score < 81 and score > 60:
#     print("학점B")
# elif score < 61 and score > 40:
#     print("학점C")
# elif score < 41 and score > 20:
#     print("학점D")
# elif score < 21 and score >= 0:
#     print("학점E")
# else:
    # print("오류")   
    
# score = int(input("점수는: "))
# if 81 <= score <= 100:
#     print("학점은 A")
# elif 61 <= score <= 80:
#     print("학점은 B")
# elif 41 <= score <= 60:
#     print("학점은 C")
# elif 21 <= score <= 40:
#     print("학점은 D")
# else:
#     print("학점은 E")