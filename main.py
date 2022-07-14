from turtle import Turtle, Screen
import random

red = Turtle()
grn = Turtle()
blu = Turtle()
ylw = Turtle()
prl = Turtle()
pnk = Turtle()

turtles = [red, pnk, prl, blu, grn, ylw]
colors = ["red", "pink", "purple", "blue", "green", "yellow"]

s = Screen()
s.setup(500, 400)

def race(y_cor):
  win = False
  winner = ""
  i = 0
  while win != True:
    t = turtles[i]
    t.fd(random.randint(1,9))
    y = y_cor[i]
    if t.pos() == (250, y):
      winner = colors[i]
      win = True
    i += 1
    if i == 6:
      i = 0
  return winner

def start():
  y = 45
  i = 0
  y_cor = [] 
  for t in turtles:
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(-250, y)
    y_cor.append(y)
    y -= 30
    i += 1
  return(race(y_cor))

def play():
  bet = s.textinput("Make your bet.", "Which turtle do you bet on? Select a colour: (red/blue/green/yellow/purple/pink)")
  winner = start()
  if winner == bet:
    result = "won"
  else:
    result = "lost"
  again = s.textinput("Play Again?", f"{winner} won the race, you {result}! do you want to play again? y/n")
  if again == "y":
    play()
  else:
    s.bye()

play()