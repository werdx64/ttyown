#!/usr/bin/env python3

import os
import glob

availablePorts=[]

while True:
  ttySearch()
  acmSerach()

def ttySearch():
  for tty in glob.glob("/dev/ttyUSB*"):
    availablePorts.append(tty)

  for usb in availablePorts:
    if acm == "ttyUSB"*
      os.system("chown werdx64 /dev/ttyUSB*")
      exit()

def acmSearch():
  for acm in glob.glob("/dev/ttyACM*"):
    availablePorts.append(acm)

  for acm in availablePorts:
    if acm == "ttyACM"*
      os.system("chown werdx64 /dev/ttyACM*")
      exit()
