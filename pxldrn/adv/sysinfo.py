import os
import time
import psutil


def getCPUtemp():
    res = os.popen('vcgencmd measure_temp').readline()
    res = res.replace("temp=", "").replace("\'", "°").rstrip()
    return(str(res))


def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])


def getCPUuse():
    # cpu = os.popen("top -n1 | awk '/%Cpu\(s\):/ {print $2}'")
    cpu = psutil.cpu_percent()
    return(str(cpu))
