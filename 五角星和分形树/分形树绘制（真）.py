import turtle


def fun(size):
    if size > 5:
        if size <= 10:
            turtle.color('green')
        turtle.forward(size)
        print('向前',size)
        turtle.right(20)
        print('右转 20')
        fun(size-15)
        turtle.left(40)
        print('左转 40')
        fun(size-15)

        turtle.right(20)
        print('右转 20')
        turtle.backward(size)
        turtle.color('brown')
        print('向后',size)


def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pencolor('brown')
    fun(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()