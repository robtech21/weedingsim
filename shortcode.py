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

import npyscreen,os,random,time
from npyscreen import wrapper_basic,Form,Popup,MultiLine,Textfield
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