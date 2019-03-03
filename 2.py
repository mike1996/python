'''


'''
import turtle
turtle.setup(600, 350, 300, 200)  # 非必须
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("red")
turtle.seth(-45)
for i in range(4):
    turtle.circle(40, 90)
    turtle.circle(-40, 90)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2//3)
turtle.done()
