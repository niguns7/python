#import library
from turtle import *
colors = ['red','yellow','blue','red','green']
for i in range(126):
    bgcolor('black')
    pencolor(colors [i % 6])
    width(i / 5 +1)
    forward(i)
    left(20)
    speed(900)
    done()