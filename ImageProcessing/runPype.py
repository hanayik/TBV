import os
import subprocess
import time
import shutil
import sys
import glob
from subprocess import call

# *************************************************
# import FSL module (if using on Hyperion cluster)
# make sure your .bash_profile has "module load fsl" (no quotes) in it so that
# fsl is loaded on every login automatically on the cluster
# *************************************************

# set up some constants
STUDY        = "Timing"
HOMEDIR      = os.environ['HOME']
STUDYDIR 	 = os.path.join(os.sep, "data", "userdata", "hanayik", STUDY) #does not have trailing slash
SUBJDIRS     = []
CORESPERSUBJ = '1'
NODESTOUSE   = '1'

print('HOMEDIR: ' + HOMEDIR)
print("STUDYDIR: " + STUDYDIR)
studyContents = glob.glob(os.path.join(STUDYDIR, 'T*'))
studyContents.sort() # make list alphabetical
print("SUBJ DIRS: ")
for sc in studyContents: # loop through the list and find subj folders
    if os.path.isdir(sc): # if its a folder then append it to the subj array
        SUBJDIRS.append(sc)
        print(sc) # print it for visual confirmation

# loop through subject folders and do processing
for subj in SUBJDIRS:
    thisSubj = os.path.basename(subj)
    cmd = ["sbatch","-p","soph", "--job-name="+thisSubj,"-n",CORESPERSUBJ,"--output",os.path.join(HOMEDIR,thisSubj+".out"),"--error",os.path.join(HOMEDIR,thisSubj+".err"),"--wrap="+"python "+os.path.join(HOMEDIR,"fslPypeHyperion.py")+" "+thisSubj]
    print(str(cmd))
    call(cmd)
 
