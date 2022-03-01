#!/usr/bin/env python3

import os
import glob

availablePorts=[]

while True:
  for file in glob.glob("/dev/ttyUSB*"):
    availablePorts.append(file)

  if len(availablePorts) > 0:
    os.system("chown werdx64 /dev/ttyUSB*")
    exit()
