#!/usr/bin/python

import os
import glob
import time
import urllib
import sys
import datetime
import xml.etree.ElementTree as ET

API_KEY='upbZ9psFuxZQwyS1L12gdX6dcHX8TTW7'

SONDES={'119':'SONDE1', '120':'SONDE3', '121':'SONDE4', '122':'SONDE5'}

# Retrieving data from WESV2
urlDATA='http://admin:wes@wesv2/data.cgx'
f = urllib.urlopen(urlDATA)
data = f.read()
root = ET.fromstring(data)

# Parsing XML format string retrieved from WES
for child in root.findall('temp'):
    for idSonde in SONDES.keys():
        temp = child.find(SONDES[idSonde]).text
        req = 'http://127.0.0.1/core/api/jeeApi.php?apikey=%s&type=virtual&id=%s&value=%s' % (API_KEY, idSonde, temp)
        handler = urllib.urlopen(req)
