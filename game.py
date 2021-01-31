#!/usr/bin/env python3

#How the heck did I go from using nano on a Raspberry Pi Zero to make basic CLI interfaces to a dual monitor setup on a PC with Visual Studio making crap like this

import shortcode
from shortcode import *
import gamevars
from gamevars import *
moneylist = [50,50,100,100,150]
Form = nps.Form

#Menu for when you first load in
def startMenu(*args):
  global choice
  F = Form(name="Start Menu")
  F.add(tft, name="Pick an option:", editable=False)
  menuChoice = F.add(MultiLine, max_height=4, scroll_exit=True, values=['New Game','Load Game','Exit'])
  F.edit()
  choice = menuChoice.value

#Exit confirmation
def confirmExit(*args):
  global choice
  F = Popup(name="Confirm Exit")
  fad = F.add
  fad(tft,name="Are you sure you want to exit?",editable=False)
  exitChoice = fad(nps.TitleText,name= "Type 'yes' or 'y' to continue:")
  F.edit()
  choice = exitChoice.value
  return choice

#Save confirmation and game saved messages
def confirmSave(*args):
  global doSave
  F = Popup(name="Confirm Save")
  F.add(tft,name="Are you sure you want to save?",editable=False)
  saveChoice = F.add(nps.TitleText,name="Type 'yes' or 'y' to continue")
  F.edit()  
  doSave = saveChoice.value
def gameSaved(*args):
  F = Popup(name="Game Saved")
  F.add(tft,name="Game saved, press enter to continue.",editable=False)
  F.edit()

#Shop message for when you don't have enough money
def notEnoughMoney(*args):
  F = Popup(name="Sorry!")
  F.add(tft,name="Not enough money!",editable=False)
  F.add(tft,name="Press Enter",editable=False)
  F.edit()

#End of day message screen 
def dayEnded(*args):
  F = Popup(name="End of Day")
  F.add(tft,name="Day Ended.",editable=False)
  F.add(tft,name="Press Enter",editable=False)
  F.edit()

#Stats Menu
def statsMenu(*args):
  F = Form(name="Game Stats")
  fad = F.add
  fad(tft,name="Current Statistics:",editable=False)
  fad(tft,name="Current Day:",value=str(daynum),editable=False)
  fad(tft,name="Strength:",value=str(strength)+"/"+str(strengthLimit),editable=False)
  fad(tft,name="EXP:",value=str(exp)+"/"+str(expRequirement),editable=False)
  percentFinished = lvl/lvlMax
  fad(tft,name="Level:",value=str(lvl)+"/"+str(lvlMax)+" ("+str(percentFinished)+"%"+" Finished)",editable=False)
  F.edit()

#A rather spooky message, more of an easter egg really
def ominousMessage1(*args):
  F = Popup(name="...")
  fad = F.add
  fad(tft,name="The sun begins to grow darker,",editable=False)
  fad(tft,name="Weeds seem to grow less quickly...",editable=False)
  fad(tft,name="-2 EXP Gain",editable=False)
  fad(tft,name="Press Enter.",editable=False)
  F.edit()

#Message for features not yet added
def notAddedYet(*args):
  F = Popup(name="Error")
  F.add(tft,name="This Feature is not added yet",editable=False)
  F.add(tft,name="Press Enter",editable=False)
  F.edit()

#Message for if you don't have enough strength to pull weeds
def notEnoughStr(*args):
  F = Popup(name="Sorry!")
  F.add(tft,name="Not enough strength",editable=False)
  F.add(tft,name="Press Enter",editable=False)
  F.edit()

#Message that prevents you from pulling weeds twice in a single day
def unableToDoThis(*args):
  F = Popup(name="Sorry!")
  fad = F.add
  fad(tft,name="You can't do this until you start a new day.",editable=False)
  fad(tft,name="Press Enter",editable=False)
  F.edit()

#Level up message
def levelUp(*args):
  F = Popup(name="Congrats!")
  fad = F.add
  fad(tft,name="You leveled up!",editable=False)
  fad(tft,name="+$"+str(moneyAmount),editable=False)
  fad(tft,name="Press Enter",editable=False)
  F.edit()

#Weed pulling results:

#Easy
def easyResults(*args):
  F = Popup(name="Results")
  fad = F.add
  fad(tft,name="-"+str(easyStrength)+" Strength",editable=False)
  fad(tft,name="+"+str(easyExpGain)+" EXP",editable=False)
  fad(tft,name="Press Enter",editable=False)
  F.edit()

#Medium
def mediumResults(*args):
  F = Popup(name="Results")
  fad = F.add
  fad(tft,name="-"+str(mediumStrength)+" Strength",editable=False)
  fad(tft,name="+"+str(mediumExpGain)+" EXP",editable=False)
  fad(tft,name="Press Enter",editable=False)
  F.edit()

#Hard
def hardResults(*args):
  F = Popup(name="Results")
  fad = F.add
  fad(tft,name="-"+str(hardStrength)+" Strength",editable=False)
  fad(tft,name="+"+str(hardExpGain)+" EXP",editable=False)
  F.edit()

#Choose maximum level for when the game ends
def preNewGame(*args):
  global lvlMax
  F = Form(name="Pregame")
  F.add(tft, name="Choose the max level:", editable=False)
  lvlMax = F.add(tt,name="Level",value="20")
  F.edit()
  lvlMax = eval(lvlMax.value)

#General menu for in-game stuff
def inGameMenu(*args):
  global choice
  F = Form(name="Game")
  fad = F.add
  def blankLine():
    fad(tft,name=" ",editable=False)
  fad(tft,name="Day:",value=str(daynum),editable=False)
  fad(tft,name="Level:",value=str(lvl),editable=False)
  fad(tft,name="Exp:",value=str(exp)+"/"+str(expRequirement),editable=False)
  fad(tft,name="Strength:",value=str(strength)+"/"+str(strengthLimit),editable=False)
  fad(tft,name="Money:",value="$"+str(money),editable=False)
  blankLine()
  fad(tft,name="Pick an option:",editable=False)
  menuChoice = fad(MultiLine, max_height=6, scroll_exit=True,values=["Pull Weeds","Shop","End Day","Save Game","View Stats","Exit"])
  F.edit()
  choice = menuChoice.value

#Menu for the shop
def shopMenu(*args):
  global shopChoice
  F = Form(name="Shop")
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
  item1cost = shovelCost
  item2cost = glovesCost
  item3cost = hormonesCost
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
  shopChoice = fad(MultiLine,max_height=3,values=["Item 1","Item 2","Item 3"],scroll_exit=True)
  F.edit()
  shopChoice = shopChoice.value

#Weed pulling menu
def weedsMenu(*args):
  #global lvl,money,expRequirement,exp,strengthLimit,easyExpGain,mediumExpGain,mediumExpGain,daynum,strength,easyStrength,mediumStrength,hardStrength,shovels,gloves,hormones,shovelCost,glovesCost,hormoneesCost,strengthGain,weedsChoice
  global weedsChoice
  F = Form(name="Pull Weeds")
  fad = F.add
  def blankLine():
    fad(tft,name=" ",editable=False)
  fad(tft, name="Easy Weeds:",editable=False,value="-"+str(easyStrength)+" Strength, +"+str(easyExpGain)+" EXP")
  fad(tft, name="Medium Weeds:",editable=False,value="-"+str(mediumStrength)+" Strength, +"+str(mediumExpGain)+" EXP")
  fad(tft, name="Hard Weeds:",editable=False, value="-"+str(hardStrength)+" Strength, +"+str(hardExpGain)+" EXP")
  blankLine()
  fad(tft, name="Choose one:",editable=False)
  weedsChoice = fad(MultiLine, max_height=4, scroll_exit=True,values=["Easy Weeds","Medium Weeds","Hard Weeds"])
  F.edit()
  weedsChoice = weedsChoice.value

#All of the magic happens here
os.system("clear")
exitChoice = False
while True:
  clr()
  if __name__ == '__main__':
    #Choose new/load game
    wrapper_basic(startMenu)
    if choice == 1:
      choice == ""
      #Imports the savefile
      import save
      from save import *
    if choice == 0:
      choice = ""
      #Choose maximum level
      wrapper_basic(preNewGame)
    canPullWeeds = True
    #Game starts here
    while lvl < lvlMax:
      endDay = False
      if exitChoice == True:
        exit()
      #Start of level up sequence
      if exp >= expRequirement:
        if exp > expRequirement:
          postExpAdd = exp - expRequirement
          exp = 0
          exp = exp + postExpAdd
          expRequirement = expRequirement + 2
        if exp == expRequirement:
          exp = 0
          expRequirement = expRequirement + 2
        moneyAmount = random.choice(moneylist)
        money = money + moneyAmount
        lvl = lvl + 1
        wrapper_basic(levelUp)
      #Just an easter egg
      if daynum == 1000:
        wrapper_basic(ominousMessage1)
        easyExpGain = easyExpGain - 2
        mediumExpGain = mediumExpGain - 2
        mediumExpGain = mediumExpGain - 2
      wrapper_basic(inGameMenu)

      #Weed pulling sequence
      if choice == 0:
        if canPullWeeds == False:
          wrapper_basic(unableToDoThis)
        if canPullWeeds == True:
          wrapper_basic(weedsMenu)
          if weedsChoice == 0:
            if strength < easyStrength:
              wrapper_basic(notEnoughStr)
            if strength >= easyStrength:
              strength = strength - easyStrength
              exp = exp + easyExpGain
              wrapper_basic(easyResults)
              canPullWeeds = False
          if weedsChoice == 1:
            if strength < mediumStrength:
              wrapper_basic(notEnoughStr)
            if strength >= mediumStrength:
              strength = strength - mediumStrength
              exp = exp + mediumExpGain
              wrapper_basic(mediumResults)
              canPullWeeds = False
          if weedsChoice == 2:
            if strength < hardStrength:
              wrapper_basic(notEnoughStr)
            if strength >= hardStrength:
              strength = strength - hardStrength
              exp = exp + hardExpGain
              canPullWeeds = False
              wrapper_basic(hardResults)
      #Shop sequence (NOT FINISHED YET)
      if choice == 1:
        wrapper_basic(shopMenu)
        if shopChoice == 2:
          wrapper_basic(notEnoughMoney)
      #End day sequence
      if choice == 2:
        endDay = True
      #Save sequence
      if choice == 3:
        wrapper_basic(confirmSave)
        if doSave == "yes" or "y":
          pnt("Saving game...\nPlease wait.")
          saveFile = open("save.py","w")
          wrt = saveFile.write
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
          vwrt("expRequirement",expRequirement)
          vwrt("exp",exp)
          vwrt("strengthLimit",strengthLimit)
          vwrt("easyExpGain",easyExpGain)
          vwrt("mediumExpGain",mediumExpGain)
          vwrt("mediumExpGain",mediumExpGain)
          vwrt("daynum",daynum)
          vwrt("strength",strength)
          vwrt("easyStrength",easyStrength)
          vwrt("mediumStrength",mediumStrength)
          vwrt("hardStrength",hardStrength)
          vwrt("shovel",shovels)
          vwrt("gloves",gloves)
          vwrt("shovelCost",shovelCost)
          vwrt("glovesCost",glovesCost)
          vwrt("lvlMax",lvlMax)
          vwrt("strengthGain",strengthGain)
          vwrt("hormonesCost",hormonesCost)
          vwrt("hormones",hormones)
          wrapper_basic(gameSaved)
          saveFile.close()
          import save
          from save import *
      #Open stats menu
      if choice == 4:
        wrapper_basic(statsMenu)
      #Exit the game
      if choice == 5:
        choice = ""
        wrapper_basic(confirmExit)
        if choice == "yes" or "y":
          exitChoice = True
      #End day sequence (continued)
      if endDay == True:
        wrapper_basic(dayEnded)
        daynum = daynum + 1
        strength = strength + strengthGain
        canPullWeeds = True
  if choice == 2:
    break
exit()
