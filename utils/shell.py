import subprocess
import os

def run(cmd):    
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def reset():
    os.system("killall -9 ccminer &> /dev/null")
    os.system("killall -9 excavator &> /dev/null")
    