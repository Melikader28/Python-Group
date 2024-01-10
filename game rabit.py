import turtle
import random
import winsound
Score=0
s =turtle.Screen()
s.setup(600,600)
s.title("بازی خرگوش و هویج")
s.bgpic('bacm5.gif')

# دیوار
wall=turtle.Turtle()
wall.up()
wall.goto(-275,275)
wall.down()
wall.width(5)
for i in range (4):
    wall.fd(550)
    wall.rt(90)
wall.ht()

#  (خرگوش)شخصیت بازی
rabbit=turtle.Turtle()
s.register_shape('rb3.gif')
rabbit.shape('rb3.gif')
rabbit.shapesize(1.5)
rabbit.up()
# هویج
carrot=turtle.Turtle()
s.register_shape("h.gif")
carrot.shape("h.gif")
carrot.up()
carrot.goto(random.randint(-260,260),random.randint(-260,260))
# امتیاز
wr=turtle.Turtle()
wr.up()
wr.goto(-270,275)
wr.ht()
wr.color('white')
wr.write('امتیاز = ' + str(Score),font=('b koodak',16,'bold'))

# توابع حرکت
def move_right():
    rabbit.right(90)
def move_left():
     rabbit.left(90)
def move_up():
    rabbit.seth(90)
    rabbit.fd(20)
def move_down():
    rabbit.seth(270)
    rabbit.fd(20)
s.listen()
s.onkey(move_right,'Right' )
s.onkey(move_left,'Left')
s.onkey(move_up,'Up')
s.onkey(move_down,'Down')

#در حال حرکت
while True:
    rabbit.fd(1)
    if rabbit.xcor()>270 or rabbit.xcor()<-270 or rabbit.ycor()>270 or rabbit.ycor()<-270:
        rabbit.right(180)
        Score=Score-5
        wr.clear()
        wr.write('امتیاز = ' + str(Score),font=('b koodak',12,'bold'))
    if rabbit.distance(carrot)<15:
        carrot.goto(random.randint(-260,260),random.randint(-260,260))
        Score = Score +10
        wr.clear()
        wr.write('امتیاز = ' + str(Score),font=('b koodak',12,'bold'))
        winsound.Beep(1000, 300)
    if Score>=20:
        wr.goto(-75,0)
        wr.write(' ،، آخجون برنده شدید :) ،،' , font=('b koodak',30,'bold'))
    if Score<=-5:
        wr.goto(-75, 0)
        wr.write('،، آخ آخ باختید :( ،، ', font=('b koodak', 30, 'bold'))
        break
turtle.mainloop()
