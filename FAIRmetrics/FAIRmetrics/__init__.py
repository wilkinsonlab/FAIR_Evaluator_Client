#-*- coding: utf-8 -*-
#!/usr/bin/env python


link = 'http://linkeddata.systems:3000'
from pprintpp import pprint as pp
import urllib2
import json


def showup(req):
    json_off = json.load(req)
    for i in json_off:
        for m in i:
                i[m] = str(i[m])
                print (m+":  "+i[m])
        print "\n"


def collections():
    req = urllib2.urlopen(link+'/collections.json')
    showup(req)

def evaluations():
    req = urllib2.urlopen(link+'/evaluations.json')
    showup(req)
    
def metrics():
    req = urllib2.urlopen(link+'/metrics.json')
    principle = raw_input("Choose your principle: (Ex. R1.1, I3 or all)")
    if "all" in principle:
        showup(req)
    else:
        json_off = json.load(req)
        for i in json_off:
            if principle.upper() == i["principle"]:
                for m in i:
                    i[m] = str(i[m])
                    print (m+":  "+i[m])
                print "\n"


