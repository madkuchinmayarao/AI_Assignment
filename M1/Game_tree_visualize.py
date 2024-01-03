import turtle
import math

def draw_node(x, y, value, alpha, beta, is_maximizing):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(20)

    turtle.penup()
    turtle.goto(x - 10, y - 25)
    turtle.pendown()
    turtle.write(f"{value}\nα={alpha}\nβ={beta}", align="center")

    if is_maximizing:
        turtle.color("red")
    else:
        turtle.color("blue")

def draw_edge(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def draw_tree():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("lightgray")

    draw_node(0, 0, 3, -math.inf, math.inf, True)

    draw_node(-50, -50, 5, -math.inf, math.inf, False)
    draw_edge(0, -20, -50, -40)

    draw_node(50, -50, 2, -math.inf, math.inf, False)
    draw_edge(0, -20, 50, -40)

    draw_node(-100, -100, 9, -math.inf, math.inf, True)
    draw_edge(-50, -70, -100, -90)

    draw_node(-80, -120, 1, -math.inf, math.inf, True)
    draw_edge(-100, -140, -80, -160)

    draw_node(20, -100, 8, -math.inf, math.inf, True)
    draw_edge(50, -70, 20, -90)

    draw_node(40, -120, 4, -math.inf, math.inf, True)
    draw_edge(20, -140, 40, -160)

    turtle.done()

if __name__ == "__main__":
    draw_tree()
