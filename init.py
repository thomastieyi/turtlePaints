#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   使用turtle库画一个动画渐变类的多边形
   @aurthor: Tony@USTB
   @Github: https://github.com/



"""
import turtle
# 引入Turtle库
import time
# 引入time库
time =time
t = turtle
# 实例化time、turtle
turtle.bgcolor("pink")
# 设置背景颜色为粉色
colors = ["red", "yellow", "green", "blue", "orange", "purple"]
# 渐变颜色数组

def draw(sides,angle):
    t.setheading(angle)
    for x in range(200):
        t.tracer(False)
        t.pencolor(colors[x % sides])
        t.forward(x * 3 / sides + x)
        t.left(360 / sides + 1)
        t.width(x * sides / 200)
        t.tracer(True)
 
   

def main():
    j=0
    t.hideturtle()
    for i in range(0,360,15):
        t.tracer(False)
        t.penup()
        t.home()
        t.pendown()
        draw((j)%5+2,i)
        j=j+1
        time.sleep(1)
        t.clear()


main()       
t.exitonclick()