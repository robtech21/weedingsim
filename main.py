#!/usr/bin/env python3
import shortcode
from shortcode import *
#splash text that I copied over from the original CLI verision
splashtxtlist = ["Colour Vision!","You'll never get to see the CLI versions uploaded on GitHub...","You can thank COVID for this game","What's 9+10?  ","Follow me @rob.amd64 on Instagram","I'm running out of splash text ideas","My life for Auir!","I hope this is entertaining","Imagine actually looking at the splash text","'Part of me, wholeheartedly.'"]
def form1(*args):
  global choice
  F = nps.Form(name="Main Menu")
  fad = F.add
  fad(tft,name=random.choice(splashtxtlist),editable=False)
  fad(tft,name="Welcome To Weeding Simulator", editable=False)
  fad(tft,name="Made By Robert Furr", editable=False)
  fad(tft,name="2021 ", editable=False)
  fad(tft,name=" ", editable=False)
  menuChoice = F.add(nps.MultiLine,max_height=4,scroll_exit=True,values=['Start','Info','Exit'])
  F.edit()
  choice = menuChoice.value
while True:
  clr()
  if __name__ == '__main__':
    nps.wrapper_basic(form1)
  if choice == 0:
    pnt("Starting game")
    os.system("./game.py")
  if choice == 1:
    pnt('''Application Info:

Version: Alpha Prototype V1
Author: Robert Furr
Year: 2021''')
    inpt("Press enter to continue")
  if choice == 2:
    break
pnt("Exited.")
exit()
