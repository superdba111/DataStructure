# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:29:54 2018

@author: yli
"""

import os
import pprint
import csv

DATADIR = "D:\downloads"
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
      
    with open(datafile, "r") as f:
         r = csv.DictReader(f)    
         for line in r:
             data.append(line)
    return data

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    pprint.pprint(d)