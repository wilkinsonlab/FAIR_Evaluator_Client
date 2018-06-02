#-*- coding: utf-8 -*-
#!/usr/bin/env python


link = 'http://linkeddata.systems:3000'
base_link = 'https://purl.org/fair-metrics/'
from .showup import showup, showin
import urllib2
import json
import requests


def metrics():
    req = urllib2.urlopen(link+'/metrics.json')
    principle = raw_input("Choose your principle: (Ex. R1.1, I3 or all)")
    if "all" in principle:
        showup(req)
    else:
        json_off = json.load(req)
        for i in json_off:
            if base_link+principle.upper() == (i["principle"]).upper():
                for m in i:
                    if type(i[m]) == list:
                        showin(i[m])
                    else:
                        i[m] = str(i[m])
                        print ("\t%s:  %s")%(m, i[m])
                print "\n"
            else:
                continue

