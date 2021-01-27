#!/usr/bin/env python3
import npyscreen,os,termcolor,random,time
from termcolor import colored
doDebug = True
color = colored
green = "green"
def clr():
  os.system("clear")
if doDebug == True:
  def clr():
    print("")
nps = npyscreen
tft = nps.TitleFixedText
tt = nps.TitleText
pnt = print
inpt = input