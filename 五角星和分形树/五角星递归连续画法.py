import turtle


def Qraw_wujiao_xing(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count+1
    size = size+20
    if size <= 200:
        Qraw_wujiao_xing(size)


def main():
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pencolor('blue')
    size = 50
    Qraw_wujiao_xing(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()