import glob
import shutil
import os

loc = raw_input("Enter Location: ")
os.chdir(loc)
Ext = raw_input("Enter Required File Extension: ")
Pre = raw_input("Enter Prefix: ")
i = 1
for f in glob.glob("*."+Ext):
    os.rename(f, "K_"+str(i)+"."+Ext)
    i += 1
i = 1
for f in glob.glob("K_*."+Ext):
    os.rename(f, Pre+"_"+str(i)+"."+Ext)
    i += 1
print str(i - 1) + " Files Renamed Successfully"
