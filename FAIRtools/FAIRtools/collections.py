#-*- coding: utf-8 -*-
#!/usr/bin/env python


link = 'http://linkeddata.systems:3000'
base_link = 'https://purl.org/fair-metrics/'
from .showup import showup, showin
import urllib2
import json
import requests


def collections():
    req = urllib2.urlopen(link+'/collections.json')
    principle = raw_input("Choose your collections id or name: (Ex. 2, \"A Metrics\" or all)")
    if "all" in principle:
        showup(req)
    else:
        json_off = json.load(req)
        for i in json_off:
            if principle == str(i["id"]) or  str(principle).upper() == (i["name"]).upper():
                for m in i:
                    if type(i[m]) == list:
                        showin(i[m])
                    else:
                        i[m] = str(i[m])
                        print ("\t%s:  %s")%(m, i[m])
                print "\n"
            else:
                continue








