import turtle

# 설정
radius = 80  # 8cm = 80mm (1cm = 10px로 가정)
side = 80    # 8cm = 80mm

t = turtle.Turtle()
t.speed(1)

# 원 그리기
t.penup()
t.goto(0, -radius)
t.pendown()
t.circle(radius)

# 정사각형 그리기
t.penup()
t.goto(-side/2, -side/2)
t.setheading(0)
t.pendown()
for _ in range(4):
    t.forward(side)
    t.left(90)

turtle.done()