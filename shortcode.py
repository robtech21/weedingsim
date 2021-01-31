#!/usr/bin/env python3
import npyscreen,os,random,time
from npyscreen import wrapper_basic,Form,Popup,MultiLine
doDebug = True
green = "green"
if doDebug == False:
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