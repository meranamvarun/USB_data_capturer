#!/usr/bin/python

import os
import commands
from time import gmtime, strftime 

destination = os.getcwd()
while True:
  folders = os.listdir("/media")
  for folder in folders:
    os.("tar -cvf /media"+folder+" "+destination+"/"+folder+"_"+strftime("%Y-%m-%d-%H-%M-%S", gmtime())+"tar.gz")
    
