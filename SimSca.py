#!/usr/bin/env python


## [Title]: SimSca.py  -- recon/enumeration script
## [Author]: FG (Technomancien)
##-------------------------------------------------------------------------------------------------------------
## [Details]: Simple Nmap vuln scanner
## 
##	Utilisation: python SimSca.py xxx.xxx.xxx.xxx
##-------------------------------------------------------------------------------------------------------------

print "############################################################"
print "####                 		                       ####"
print "####                   SimSca	         	       ####"
print "####         					       ####"
print "############################################################"

"requirements : nmap,xsltproc and vulners.nse"

import sys
import os
import subprocess




if len(sys.argv) != 2:
   print " Put a IP address !!!"
   sys.exit(0)



ip_address = sys.argv[1] 
print "INFO: python SimSca.py " + ip_address
print "Go get a coffee it might take some time ..."
SCAN = "nmap -vv -sS -Pn -A -sV -T4 --script=default,auth,vuln,discovery,vulners -p- -oX scan.xml --script-args=safe=1 %s" %(ip_address) 
results = subprocess.check_output(SCAN, shell=True) 

if results != "":
	Transfert = "xsltproc scan.xml -o " + ip_address + "_scan.htm"
	results2 = subprocess.check_output(Transfert, shell=True)
	os.remove('scan.xml')

print "###############################################################################"

print "INFO: Nmap scans completed for "  + ip_address 

print "###############################################################################"

 

