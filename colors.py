import turtle as t
import colorsys as c
t.setup(1537,865)
q=0
t.tracer(200)
t.bgcolor('black')
t.width(2)
for i in range(2000):
    q+=0.01
    color=c.hsv_to_rgb(q,1,1)
    t.pencolor(color)

    t.fd(i)
    t.rt(200)
    t.fd(i)
    t.rt(222)
    t.fd(i)
    t.circle(i,-210)
t.done()