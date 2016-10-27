#!/usr/bin/python python3
import subprocess 
import shlex 
import time
import json

def getJson(vFile):
    # Open json file
    with open('data/' + vFile) as data_file:
        data = json.load(data_file)

    # How many rows?
    dataL = data["meta"]["legend"]
    nrRange = len(dataL)

    # First fix the data
    dataJ = data["data"]
    dataJ.pop()
    transposed = []
    for i in range(nrRange):
        i = int(float(i))
        transposed.append([row[i] for row in dataJ])

    flist = ( ", ".join( repr(e) for e in transposed ) )
    flist = flist.replace("None", "0")

    # Now for the legends
    #dataL = data["meta"]["legend"]
    for i, v in enumerate(dataL):
        flist = flist.replace("[", "$'" + v + "', ", 1)

    flist = flist.replace("$", "[")
    flist = flist.replace("]", "], ")
    flist = flist.replace("], ,", "], ")
    flist = flist[:-1]

    # Now for epoch time
    dataStart = data["meta"]["start"]
    dataEnd = data["meta"]["end"]
    dataStep = data["meta"]["step"]
    nE = dataStart
    timestamp = ''
    while nE != (dataEnd - dataStep):
        nE = nE + dataStep
        #timestamp = timestamp + str(nE) + ", "
        timestamp = timestamp + "'" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(nE)) + "', "
    timestamp = timestamp[:-2]
    #timestamp = "['x', " + str(dataStart) + ", " + timestamp
    timestamp = "['x', " + timestamp
    timestamp = timestamp + "], "


    return timestamp + flist


# Run bash script and collect data
def run_commandOnce(command):
    try:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            return ("Fail")
        if output:
            return output.strip()

    except:
        return "Fail"

