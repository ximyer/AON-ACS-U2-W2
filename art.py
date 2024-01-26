import turtle

tu = turtle.Turtle()
tu.screen.bgcolor('#8EACCD')
tu.pensize(2)
tu.color('#F9F3CC')
tu.left(90)
tu.backward(100)
tu.speed(100)
tu.shape('turtle')

def tree(i):
     if i > 10:
          tu.forward(i)
          tu.color('#D7E5CA')
          tu.circle(2)
          tu.color('#F9F3CC')
          tu.left(30)
          tree(3 * i / 4)
          tu.right(60)
          tree(3 * i / 4)
          tu.left(30)
          tu.backward(i)

tree(80)
turtle.mainloop()