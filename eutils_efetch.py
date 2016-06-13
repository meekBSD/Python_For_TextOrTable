#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
import socket, time

print os.getcwd()

ID_list = [a.rstrip() for a in open("nocl_id.txt",'r').readlines()]
ID_set = set(ID_list)

base = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
## search = {"db": "taxonomy", "id": "2057", "retmode":"xml"}
## efetch.fcgi?db=nuccore&id=25026556&rettype=fasta&retmode=text   // other ID example  HQ914928

user_agent="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {'User-Agent':user_agent}

output = open("tax_result.txt",'w')

timeout = 5
socket.setdefaulttimeout(timeout)
sleep_download_time = 3

for order_id in ID_set:                  # Here use the set of taxonomy ID, without duplicate ids
    
    search = {"db": "taxonomy", "id": order_id, "retmode":"xml"}
    values = urllib.urlencode(search)
    try:
        time.sleep(sleep_download_time)
        request = urllib2.Request(base, values, headers)
        response = urllib2.urlopen(request)
        page = response.read()
        response.close()
    except UnicodeDecodeError as e:
        print ('------UnicodeDecodeError url:', order_id)
        page = None
    except urllib2.URLError as e:
        print ('------urlError url:',order_id)
        page = None
    except socket.timeout as e:
        print ('------socket timeout:', order_id)
        page = None
    
    try:
        soup = BeautifulSoup(page)
        #print soup.prettify()

        lineage = str(soup.taxaset.lineage.contents[0])
        #print lineage
        line = lineage.split("; ")
        line.reverse()
        rever_line = line
        #print [order_id, ";".join(rever_line)]
        output.write("\t".join([order_id, ";".join(rever_line)])+"\n")
    except NameError, msg:
        print ('------ %s %s'% (order_id,msg) )
    except TypeError, msg1:
        print ('------ %s %s'% (order_id, msg1))

output.close()
