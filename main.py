#!/usr/bin/env python3

# Part of my Weeding Simulator game
# Copyright (C) 2021 Robert Furr

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from appmodules.shortcode import *
os.system("clear")
#splash text that I copied over from the original CLI verision
splashtxtlist = ["You can thank COVID for this game","My Life for Aiur!","What's 9+10?","Follow me @rob.amd64 on Instagram","I'm running out of splash text ideas","I hope this is entertaining","Imagine actually looking at the splash text","Part of me, wholeheartedly."]

#This crashes your game sometimes if your terminal isn't big enough
def aboutMenu(*args):
  F = nps.Form(name="About")
  fad = F.add
  def addLine(text):
    fad(Textfield,value=('  '+text),editable=False)
  def newLine():
    addLine(' ')
  fad(tft,name="  Version Info:",editable=False)
  addLine('=====')
  addLine('Name:     Alpha Version 2')
  addLine('Author:   Robert Furr (robert@megley.com)')
  addLine('License:  GPL3')
  addLine('Year:     2021')
  addLine('Date:     2/22/2021')
  addLine('=====')
  newLine()
  fad(tft,name="  Copyright Info:",editable=False)
  addLine('=====')
  addLine('My Weeding Simulator Game')
  addLine('Copyright (C) 2021  Robert Furr (robert@megley.com)')
  newLine()
  addLine('This program is free software: you can redistribute it and/or modify')
  addLine('it under the terms of the GNU General Public License as published by')
  addLine('the Free Software Foundation, either version 3 of the License, or')
  addLine('(at your option) any later version.')
  newLine()
  addLine('This program is distributed in the hope that it will be useful,')
  addLine('but WITHOUT ANY WARRANTY; without even the implied warranty of')
  addLine('MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the')
  addLine('GNU General Public License for more details.')
  newLine()
  addLine('You should have received a copy of the GNU General Public License')
  addLine('along with this program.  If not, see <https://www.gnu.org/licenses/>.')
  addLine('=====')
  newLine()  
  addLine('Press enter to return to title')
  F.edit()
def form1(*args):
  global choice
  splashtext = random.choice(splashtxtlist)
  F = nps.Form(name="Main Menu - "+str(splashtext))
  fad = F.add
  fad(tft,name="Welcome To Weeding Simulator", editable=False)
  fad(Textfield,value="Alpha V2",editable=False)
  fad(Textfield,value="Made By Robert Furr", editable=False)
  fad(Textfield,value="2021 ", editable=False)
  fad(tft,name=" ", editable=False)
  fad(tft,name="===",editable=False)
  fad(tft,name=" ", editable=False)
  menuChoice = F.add(nps.MultiLine,max_height=5,scroll_exit=True,values=['Start','About',"Join the Discord",'Exit'])
  F.edit()
  choice = menuChoice.value
while True:
  clr()
  if __name__ == '__main__':
    wrapper_basic(form1)
  if choice == 0:
    pnt("Starting game")
    os.system("./game.py")
  if choice == 1:
    clr()
    wrapper_basic(aboutMenu)
  if choice == 2:
    openLink = inpt("Would you like to open the Discord link in your browser? (y/n)\n>")
    if openLink == "y":
      pnt("Running xdg-open. Your browser will open soon.")
      os.system("xdg-open https://discord.gg/Demm836 &>/dev/null")
      inpt("Press enter to go back to title\n")
  if choice == 3:
    break
pnt("Exited.")
exit()
