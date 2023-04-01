import turtle
import winsound

w=turtle.Screen()
w.bgcolor("black")
w.setup(width=800,height=600)
w.tracer(0)
w.listen()
c=0
life=3
#pad
pad=turtle.Turtle()
pad.speed(0)
pad.color("green")
pad.shape("square")
pad.shapesize(stretch_len=7,stretch_wid=1)
pad.penup()
pad.goto(0,-270)
#ball
ball=turtle.Turtle()
ball.color("yellow")
ball.shape("circle")
ball.penup()
ball.dx=0.2          #adjust to your preffered speed
ball.dy=0.2
#pen
pen=turtle.Turtle()
pen.penup()
pen.color("white")
pen.goto(0,260)
pen.speed(0)
pen.hideturtle()
pen.write("Score: 0  Life: 3",align="center",font=("Aardvark",25,"bold"))
#function1
def pad_right():
    x=pad.xcor()
    x+=20
    pad.setx(x)
w.onkeypress(pad_right,"Right")
#function2
def pad_left():
    x=pad.xcor()
    x-=20
    pad.setx(x)
w.onkeypress(pad_left,"Left")
#loop 
while True:
    w.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if (ball.xcor()>385):
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.dx*=-1
    if (ball.xcor()<-385):
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (ball.ycor()>290):
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (ball.ycor()<-290):
        ball.dy*=-1
        ball.setx(0)
        ball.sety(0)
        life-=1
        pen.clear()
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        pen.write("Score: {}  Life: {}".format(c,life),align="center",font=("Aardvark",25,"bold"))
    if (ball.xcor()<pad.xcor()+70 and ball.xcor()>pad.xcor()-70) and (ball.ycor()<-250):
        ball.dy*=-1
        ball.sety(-250)    
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        c+=1
        pen.clear()
        pen.write("Score: {}  Life: {}".format(c,life),align="center",font=("Aardvark",25,"bold"))
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if life==0:
        break
   
       
        
        
        
    
