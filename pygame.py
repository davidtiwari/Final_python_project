import turtle
import random
import time

delay=0.1
score=0
heighestscore=0

#snakebodies
bodies=[]

#getting a screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600,height=600)

#creating snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#score board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0  |  Heighest Score:  0")

def moveup() :
    if head.direction!="down":
        head.direction="up"
def movedown() :
    if head.direction!="up":
        head.direction="down"
def moveleft() :
    if head.direction!="right":
        head.direction="left"
def moveright() :
    if head.direction!="left":
        head.direction="right"
def movestop() :
    head.direction="stop"
