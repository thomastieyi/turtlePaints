#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   @Description:使用turtle库画一个动画渐变类的多边形
   @Aurthor: Tony@USTB
   @Github: https://github.com/thomastieyi/turtlePaints
   @Required_ENV: Pythin-2.7
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
    """
       @Description:绘制单个颜色渐变的多变形，可以根据输入选择来绘制不同的形状.
       @Input: {int} sides (0<sides<6) 绘制边数; {int} angle (0<angle<360) 绘制初始角度.
       @Output: Graphs.
    """
    t.setheading(angle)   
    # 设置启示角度
    for x in range(200):
        # 循环次数代表这多边形的饱满程度
        t.tracer(False)
        # 隐藏画图轨迹
        t.pencolor(colors[x % sides])
        # 设置渐变的颜色
        t.forward(x * 3 / sides + x)
        t.left(360 / sides + 1)
        t.width(x * sides / 200)
        # 绘制
        t.tracer(True)
 
   

def main():
    """
       @Description:利用for循环一次绘制颜色渐变的多变形.
       @Input: None.
       @Output: Graphs.
    """
    j=0
    t.hideturtle()
    # 隐藏乌龟
    for i in range(0,360,15):
        # 画图
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