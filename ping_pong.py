import turtle as t
import os

playerAscore=0
playerBscore=0

window=t.Screen()
window.title("PING-PONG GAME")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)


#creating the left paddle

leftPaddle= t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("red")
leftPaddle.shapesize(stretch_len=1,stretch_wid=5)
leftPaddle.penup()
leftPaddle.goto(-350,0)

#creating the right paddle

rightPaddle= t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("red")
rightPaddle.shapesize(stretch_len=1,stretch_wid=5)
rightPaddle.penup()
rightPaddle.goto(350,0)

#creating ball

ball = t.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ballxdirection=0.5
ballydirection=0.5


# creating pen for scorecard update

pen= t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                Player B: 0",align="center",font=('Arial',24,'normal'))



# moving leftpaddle

def leftpaddleup():
    y=leftPaddle.ycor()
    y= y+20
    leftPaddle.sety(y)


def leftpaddledown():
    y=leftPaddle.ycor()
    y= y-20
    leftPaddle.sety(y)



#moving the right paddle

def rightpaddleup():
    y=rightPaddle.ycor()
    y= y+20
    rightPaddle.sety(y)


def rightpaddledown():
    y=rightPaddle.ycor()
    y= y-20
    rightPaddle.sety(y)



window.listen()
window.onkeypress(leftpaddleup,'u')
window.onkeypress(leftpaddledown,'d')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')


while True:
    window.update()
    
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    #settingup border

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerAscore= playerAscore+1
        pen.clear()
        pen.write("Player A:{}    Player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))
        os.system("afplay wallhit.wav&")


    if ball.xcor() < -390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerBscore= playerBscore+1
        pen.clear()
        pen.write("Player A:{}    Player B:{}".format(playerAscore,playerBscore),align='center',font=('Arial',24,'normal'))
        os.system("afplay wallhit.wav&")



    #handling the collisions

    if(ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightPaddle.ycor()+40 and ball.ycor()>rightPaddle.ycor()-40):
      ball.setx(340)
      ballxdirection= ballxdirection*-1
      os.system("afplay paddle.wav&")

    if(ball.xcor()<-340)and(ball.xcor()>-350)and(ball.ycor()<leftPaddle.ycor()+40 and ball.ycor()>leftPaddle.ycor()-40):
      ball.setx(-340)
      ballxdirection= ballxdirection*-1
      os.system("afplay paddle.wav&")
