from turtle import Turtle, Screen, colormode
import random

########### Challenge 5 - Draw Spirograph ########

tim = Turtle()
colormode(255)
tim.shape("turtle")
tim.speed("fastest")
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

def draw_spirograph(size_of_gap):
  for _ in range(int(360 / size_of_gap)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()