import turtle
import winsound
w1=turtle.Screen()
w1.bgcolor("green")
w1.setup(width=800,height=600)
w1.tracer(0)
#score
score1=0
score2=0
#bar left
bar_1=turtle.Turtle()
bar_1.speed(0)
bar_1.shape("square")
bar_1.shapesize(stretch_wid=6,stretch_len=1)
bar_1.color("red")
bar_1.penup()
bar_1.goto(-350,0)
#bar right
bar_2=turtle.Turtle()
bar_2.speed(0)
bar_2.shape("square")
bar_2.shapesize(stretch_wid=6,stretch_len=1)
bar_2.color("blue")
bar_2.penup()
bar_2.goto(350,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center", font=("Agency FB",25,"normal"))
#function1
def bar_1_up():
    y=bar_1.ycor()
    y+=20
    bar_1.sety(y)
w1.listen() #listen for keyboard input
w1.onkeypress(bar_1_up,"w")
#function2
def bar_2_up():
    y=bar_2.ycor()
    y+=20
    bar_2.sety(y)
w1.listen() #listen for keyboard input
w1.onkeypress(bar_2_up,"o")
#function3
def bar_1_down():
    y=bar_1.ycor()
    y-=20
    bar_1.sety(y)
w1.listen() #listen for keyboard input
w1.onkeypress(bar_1_down,"s")
#function4
def bar_2_down():
    y=bar_2.ycor()
    y-=20
    bar_2.sety(y)
w1.listen() #listen for keyboard input
w1.onkeypress(bar_2_down,"l")

#game loop
while True:
    w1.update()

    ball.setx(ball.xcor()+ball.dx) #moving ball
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor()>290:            #border check
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor()<-290:            #border check
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()>390:            #border check
        ball.goto(0,0)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        score1+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score1,score2),align="center", font=("Agency FB",25,"normal"))
    if ball.xcor()<-390:            #border check
        ball.goto(0,0)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        score2+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score1,score2),align="center", font=("Agency FB",25,"normal"))
    
    if (ball.xcor()>335 and ball.xcor()<350) and (ball.ycor()<bar_2.ycor()+60 and ball.ycor()>bar_2.ycor()-60):
        ball.setx(335)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (ball.xcor()<-335 and ball.xcor()>-350) and (ball.ycor()<bar_1.ycor()+60 and ball.ycor()>bar_1.ycor()-60):
        ball.setx(-335)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)