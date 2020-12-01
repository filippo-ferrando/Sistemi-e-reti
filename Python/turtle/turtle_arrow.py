from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor('lightblue')

#pointer creation
pointer = Turtle()
pointer.color('red')
pointer.penup()

wn.setup(width=800, height=800)

#define speed
speed = 3

#travel function (control pointer speed and border over)
def travel():
    pointer.forward(speed)
    wn.ontimer(travel, 10)

    if pointer.xcor() > 390 or pointer.xcor() < -390:
        pointer.goto(0,0)
    #pointer.direction = "stop"

    if pointer.ycor() > 390 or pointer.ycor() < -390:
        pointer.goto(0,0)

#command for arrow keys
wn.onkey(lambda: pointer.setheading(90), 'Up')
wn.onkey(lambda: pointer.setheading(180), 'Left')
wn.onkey(lambda: pointer.setheading(0), 'Right')
wn.onkey(lambda: pointer.setheading(270), 'Down')

#listen for arrow keys
wn.listen()

#call travel function
travel()

#loop instruction
wn.mainloop()
