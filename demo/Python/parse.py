#!/usr/bin/python3
import re, os

def iterateOverDir(fdir, grep):
    """
    fdir: folder name
    grep: "CPU [0-9] cumulative IPC:.*"
    """
    dic = {}
    for fname in os.listdir(fdir):
        #name = fname.split('---')[0] 
        name = fname            # file name

        # print("Traversing:", fname)
        # input("Pause Here!!")

        if name not in dic:
            dic[name] = []
        dic[name].append(readFile("{}/{}".format(fdir, fname), grep))
    return dic

def readFile(fname, grep):
    """
    fname: file name
    grep: "CPU [0-9] cumulative IPC:.*"
    """
    with open(fname) as f:
        raw = f.read()
        line = re.findall(grep, raw)
    
    # print("Found line:", line)
    # input("Pause Here!!")

    return line

