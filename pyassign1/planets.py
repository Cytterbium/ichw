import math
import turtle 
xz=turtle.Turtle()
wn=turtle.Screen()
wn.title('welcome to the solar system!')
wn.bgcolor('black')
wn.setworldcoordinates(-500,-500,750,750)
xz.color('red')
xz.speed(0)
xz.shape("circle")
xz.up()
xz.goto(-30,0)
xz.down()

a1=70;b1=48

a=xz.clone()
a.color('blue')
a.up()
a.goto(0,b1)
a.down()

b=xz.clone()
b.color('green')
b.up()
b.goto(20,1.5*b1)
b.down()
b.lt(90)

c=xz.clone()
c.color('yellow')
c.up()
c.goto(30,1.9*b1)
c.down()
c.lt(180)

d=xz.clone()
d.color('purple')
d.up()
d.goto(44,2.4*b1)
d.down()
d.rt(90)

e=xz.clone()
e.color('orange')
e.up()
e.goto(60,3.0*b1)
e.down()

f=xz.clone()
f.color('pink')
f.up()
f.goto(70,4.0*b1)
f.down()
f.lt(180)

for t in range(30000):
    a.goto(a1*math.sin(t/10),b1*math.cos(t/10))
    b.goto(1.5*(a1*math.sin(t/20))+20,1.5*(b1*math.cos(t/20)))
    c.goto(1.9*(a1*math.sin(t/30))+30,1.9*(b1*math.cos(t/30)))
    d.goto(2.4*(a1*math.sin(t/40))+44,2.4*(b1*math.cos(t/40)))  
    e.goto(3*(a1*math.sin(t/60))+60,3*(b1*math.cos(t/60)))
    f.goto(4*(a1*math.sin(t/80))+70,4*(b1*math.cos(t/80)))
 
