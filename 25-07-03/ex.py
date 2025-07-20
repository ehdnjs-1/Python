import turtle
t = turtle.Turtle() # turtle의 기능을 t라고 부르겠다.
t.shape("turtle")

# 사용자로부터 집의 크기를 받아서 size라는 변수에 저장한다.
size = int(input("집의 크기는 얼마로 할까요? "))

t.left(60)
t.forward(size) # 1
t.right(120)
t.forward(size) # 2
t.right(30)
t.forward(size) # 3
t.right(90)
t.forward(size) # 4
t.right(90)
t.forward(size) # 5
t.right(90)
t.forward(size) # 6

turtle.done()