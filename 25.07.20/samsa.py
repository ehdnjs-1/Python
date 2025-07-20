import turtle

t = turtle.Turtle()
t.speed(0)

for _ in range(5):
    # 삼각형 그리기 (빨간색)
    t.color("red")
    t.begin_fill()
    for _ in range(3):
        t.forward(50)
        t.right(120)
    t.end_fill()
    t.penup()
    t.forward(80)  # 다음 도형을 위해 오른쪽으로 이동
    t.pendown()
    
    # 사각형 그리기 (파란색)
    t.color("blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.penup()
    t.forward(80)  # 다음 반복을 위해 오른쪽으로 이동
    t.pendown()

turtle.done()