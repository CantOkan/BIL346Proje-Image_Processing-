import turtle
import time
import random

def start():
    window=turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("white")

    img = "xapple.gif"

    window.addshape(img)

    window.setup(width=600,height=600)
    window.tracer(0)


    score=0
    HighScore=0

    #Snake head

    head=turtle.Turtle()
    head.speed(speed=0)#animation speed
    head.shape("square")
    head.color("black")
    head.penup()

    head.goto(0,0)

    head.direction="stop"

    def reset():
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
    # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)



    def up():
        if head.direction !="down":
            head.direction ="up"

    def left():
        if head.direction !="right":
            head.direction="left"

    def right():
        if(head.direction!="left"):
            head.direction="right"

    def down():
        if(head.direction!="up"):
            head.direction="down"



    def move():
        if(head.direction=="up"):
            y=head.ycor()
            head.sety(y+10)

        elif(head.direction=="down"):
            y=head.ycor()
            head.sety(y-10)

        elif(head.direction=="left"):
            x=head.xcor()
            head.setx(x-10)

        elif(head.direction=="right"):
            x=head.xcor()
            head.setx(x+10)

    def newfood():
        x=random.randint(-190,190)
        y=random.randint(-190,190)
        food.goto(x,y)

    #Food
    food=turtle.Turtle()
    food.speed(speed=0)
    food.shape(img)
    food.width(10)

    food.penup()
    food.goto(100, 0)

    def catch():
        new_segment=turtle.Turtle()
        new_segment.speed(speed=0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

    def startAgain():
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

    segments=[]



    #PEN
    pen=turtle.Turtle()
    pen.speed(speed=0)
    pen.shape("square")
    pen.color("Black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,270)
    pen.write("Score :{} High Score:{}".format(score,HighScore),align="center",font=("Arial", 24, "normal"))


    window.onkeypress(up,"w")# OK tuşları içi "UP"
    window.onkeypress(left,"a")
    window.onkeypress(right,"d")
    window.onkeypress(down,"s")
    window.onkeypress(reset,"r")



    window.listen()

    while  True:
        window.update()


        if(head.distance(food)<20):#Yemek yakalandımı
            pen.clear()
            score+=1
            if(HighScore<score):
                HighScore=score
            pen.clear()
            pen.write("Score :{} High Score:{}".format(score,HighScore),align="center",font=("Arial", 24, "normal"))


            #yeniden food yarat
            #Snake uzasın
            newfood()
            catch()

        for index in range(len(segments)-1, 0,-1):
            x=segments[index-1].xcor()
            y=segments[index-1].ycor()

            segments[index].goto(x,y)

        if(len(segments)>0):
            x=head.xcor()
            y=head.ycor()
            segments[0].goto(x,y)


        move()

        for segment in segments:
            if(segment.distance(head)<10):
                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"
            # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()
                score=0

        time.sleep(0.2)#Delay

    window.mainloop()


start()
