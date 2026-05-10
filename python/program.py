## main program

## import libraries
import tkinter as tkr
import math as mat
import os as osf
import sys
import pathlib as ptl
import logging as lig
import argparse as arp
import json as jso
import datetime as dat
import time as tim
import typing as typ
import collections as col
import functools as fnc
import itertools as irt
import subprocess as sbp
import contextlib as ctx
import tempfile as tmp
import shutil as shu
import re as rge
import statistics as sta
import hashlib as hlb
import hmac as hmc
import secrets as sct
import socket as skt
import urllib as url
## yes this is excessive lol

## set variables
drive = "nothing"
answer1 = "nothing"
path = "nothing"
folderLoc = "nothing"

## code

print("This is an early test program. This will not do anything and is, as it stands, a stub.")
print("Currently this is only used to test some basic logic and code. This is purely a test and no actions will really be taken.")
print("")
print("Please provide a drive letter, without any colons or slashes.")
drive = str(input(">"))
print("Is this a rockbox player, or is it something else? (R = rockbox, O = other. Case insensitive.)")
answer1 = str(input(">"))
if answer1 == "R" or answer1 == "r":
    print("The program would have accessed " + drive + ":/.rockbox - this is a rockbox player.")
    path = (drive + ":/.rockbox")
elif answer1 == "O" or answer1 == "o":
    print("Now point to the location of the folder. This should be in the format of '/folder/subfolder/'. Slash is mandatory.")
    folderLoc = str(input(">"))
    path = (drive + ":" + folderLoc)
    print("The program would have accessed " + path + ", as you provided a folder.")
else:
    print("that was not a correct choice, please restart the test.")
    tim.sleep(10000)

## that's it for now