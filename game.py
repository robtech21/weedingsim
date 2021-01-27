#!/usr/bin/env python3

#How the heck did I go from using nano on a Raspberry Pi Zero to make basic CLI interfaces to a dual monitor setup on a PC with Visual Studio making crap like this
#Also how can I enjoy this only at late at night with caffiene in my system and rain sounds playing via the "Blanket" application

import shortcode
from shortcode import *
import gamevars
from gamevars import *
def startMenu(*args):
  global choice
  F = nps.Form(name="Start Menu")
  F.add(tft, name="Pick an option:", editable=False)
  menuChoice = F.add(nps.MultiLine, max_height=4, scroll_exit=True, values=['New Game','Load Game','Exit'])
  F.edit()
  choice = menuChoice.value
def confirmExit(*args):
  global choice
  F = nps.Popup(name="Confirm Exit")
  fad = F.add
  fad(tft,name="Are you sure you want to exit?",editable=False)
  exitChoice = fad(nps.TitleText,name= "Type 'yes' or 'y' to continue:")
  F.edit()
  choice = exitChoice.value
  return choice
def confirmSave(*args):
  global doSave
  F = nps.Popup(name="Confirm Save")
  F.add(tft,name="Are you sure you want to save?",editable=False)
  saveChoice = F.add(nps.TitleText,name="Type 'yes' or 'y' to continue")
  F.edit()
  doSave = saveChoice.value
def gameSaved(*args):
  F = nps.Popup(name="Popup")
  F.add(tft,name="Game saved, press enter to continue.",editable=False)
  F.edit()
def notEnoughMoney(*args):
  F = nps.Popup(name="Sorry!")
  F.add(tft,name="Not enough money!",editable=False)
  F.edit()  
def dayEnded(*args):
  F = nps.Popup(name="End of Day")
  F.add(tft,name="Day Ended.",editable=False)
  F.add(tft,name="Press Enter",editable=False)
  F.edit()
def notAddedYet(*args):
  F = nps.Popup(name="Error")
  F.add(tft,name="This Feature is not added yet",editable=False)
  F.add(tft,name="Press Enter",editable=False)
  F.edit()
def preNewGame(*args):
  global lvlmax
  F = nps.Form(name="Pregame")
  F.add(tft, name="Choose the max level:", editable=False)
  lvlmax = F.add(tt,name="Level",value="20")
  F.edit()
  lvlmax = eval(lvlmax.value)
def inGameMenu(*args):
  global choice,lvl,money,exprequirement,exp,strengthlimit,easyexpgain,mediumexpgain,hardexpgain,daynum,strength,easystrength,mediumstrength,hardstrength,shovels,gloves,hormones,shovelcost,glovescost,hormonescost,strengthgain
  F = nps.Form(name="Game")
  fad = F.add
  def blankLine():
    fad(tft,name=" ",editable=False)
  fad(tft,name="Day:",value=str(daynum),editable=False)
  fad(tft,name="Level:",value=str(lvl),editable=False)
  fad(tft,name="Exp:",value=str(exp)+"/"+str(exprequirement),editable=False)
  blankLine()
  fad(tft,name="Pick an option:",editable=False)
  menuChoice = fad(nps.MultiLine, max_height=5, scroll_exit=True,values=["Pull Weeds","Shop","Skip to Next Day","Save Game","Exit"])
  F.edit()
  choice = menuChoice.value
def shopMenu(*args):
  global lvl,money,exprequirement,exp,strengthlimit,easyexpgain,mediumexpgain,hardexpgain,daynum,strength,easystrength,mediumstrength,hardstrength,shovels,gloves,hormones,shovelcost,glovescost,hormonescost,strengthgain,shopChoice
  F = nps.Form(name="Shop")
  fad = F.add
  def div():
    fad(tft,name="=====",editable=False)
  def blankLine():
    fad(tft,name=" ",editable=False)
  fad(tft, name="Your balance:",value="$"+str(money),editable=False)
  fad(tft, name="Items for sale:",editable=False)
  div()
  #these exist purely for adaptability for when I add random items/prices :)
  item1 = "Shovel"
  item2 = "Gloves"
  item3 = "Hormones"
  item1amount = shovels
  item2amount = gloves
  item3amount = hormones
  item1cost = shovelcost
  item2cost = glovescost
  item3cost = hormonescost
  def shopItem(number,itemName,itemCost,itemAmount):
    fad(tft,name="Item "+number+":",editable=False)
    fad(tft,name="Name:",value=itemName,editable=False)
    fad(tft,name="Price:",value="$"+str(itemCost),editable=False)
    fad(tft,name="Owned:",value=str(itemAmount),editable=False)
  shopItem("1",item1,item1cost,item1amount)
  blankLine()
  shopItem("2",item2,item2cost,item2amount)
  blankLine()
  shopItem("3",item3,item3cost,item3amount)
  div()
  fad(tft,name="Choose an item:",editable=False)
  shopChoice = fad(nps.MultiLine,max_height=3,values=["Item 1","Item 2","Item 3"],scroll_exit=True)
  F.edit()
  shopChoice = shopChoice.value
def weedsMenu(*args):
  global lvl,money,exprequirement,exp,strengthlimit,easyexpgain,mediumexpgain,hardexpgain,daynum,strength,easystrength,mediumstrength,hardstrength,shovels,gloves,hormones,shovelcost,glovescost,hormonescost,strengthgain
  F = nps.Form(name="Pull Weeds")
  fad = F.add
  def blankLine():
    fad(tft,name=" ",editable=False)
  fad(tft, name="Easy Weeds:",editable=False,value="-"+str(easystrength)+" Strength, +"+str(easyexpgain)+" EXP")
  fad(tft, name="Medium Weeds:",editable=False,value="-"+str(mediumstrength)+" Strength, +"+str(mediumstrength)+" EXP")
  fad(tft, name="Hard Weeds:",editable=False)
  blankLine()
  fad(tft, name="Choose one:",editable=False)
  menuChoice = fad(nps.MultiLine, max_height=4, scroll_exit=True,values=["Easy Weeds","Medium Weeds","Hard Weeds"])
  F.edit()
  choice = menuChoice.value
os.system("clear")
exitChoice = False
while True:
  clr()
  if __name__ == '__main__':
    nps.wrapper_basic(startMenu)
    if choice == 0:
      choice = ""
      nps.wrapper_basic(preNewGame)
      while lvl < lvlmax:
        endDay = False
        if exitChoice == True:
          exit()
        nps.wrapper_basic(inGameMenu)
        if choice == 0:
          nps.wrapper_basic(weedsMenu)
        if choice == 1:
          nps.wrapper_basic(shopMenu)
          if shopChoice == 2:
            nps.wrapper_basic(notEnoughMoney)
        if choice == 2:
          endDay = True
        if choice == 3:
          #nps.wrapper_basic(notAddedYet)
          nps.wrapper_basic(confirmSave)
          if doSave == "yes" or "y":
            savefile = open("save.py","w")
            wrt = savefile.write

            def nl():
              wrt("\n")
            def vwrt(valuename,value):
              nl()
              wrt(str(valuename)+'='+str(value))
            wrt("#!/usr/bin/env python3")
            nl()
            wrt("#Save file that can be imported into the game")
            nl()
            time.sleep(0.5)
            vwrt('lvl',lvl)
            vwrt("money",money)
            vwrt("exprequirement",exprequirement)
            vwrt("exp",exp)
            vwrt("strengthlimit",strengthlimit)
            vwrt("easyexpgain",easyexpgain)
            vwrt("mediumexpgain",mediumexpgain)
            vwrt("hardexpgain",hardexpgain)
            vwrt("daynum",daynum)
            vwrt("strength",strength)
            vwrt("easystrength",easystrength)
            vwrt("mediumstrength",mediumstrength)
            vwrt("hardstrength",hardstrength)
            vwrt("shovel",shovels)
            vwrt("gloves",gloves)
            vwrt("shovelcost",shovelcost)
            vwrt("glovescost",glovescost)
            vwrt("lvlmax",lvlmax)
            vwrt("strengthgain",strengthgain)
            vwrt("hormonescost",hormonescost)
            vwrt("hormones",hormones)
            #inpt(color("Game Saved","yellow"))
            nps.wrapper_basic(gameSaved)
            savefile.close()
            import save
            from save import *
        if choice == 4:
          choice = ""
          nps.wrapper_basic(confirmExit)
          if choice == "yes" or "y":
            exitChoice = True
        if endDay == True:
          nps.wrapper_basic(dayEnded)
          daynum = daynum + 1
  if choice == 1:
    nps.wrapper_basic(notAddedYet)
  if choice == 2:
    break
exit()
