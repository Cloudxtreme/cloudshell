#!/usr/bin/env python

import pyrax
from cloudfunctions import listservers
from cloudfunctions import createservers
from cloudfunctions import connectServer
import os
import time

def menu():
    print """
    Welcome to CloudShell v0.1.0
    
     .--. .-.    .--. .-..-..---.  .--. .-..-. .--. .-.   .-.   
    : .--': :   : ,. :: :: :: .  :: .--': :; :: .--': :   : :   
    : :   : :   : :: :: :: :: :: :`. `. :    :: `;  : :   : :   
    : :__ : :__ : :; :: :; :: :; : _`, :: :: :: :__ : :__ : :__ 
    `.__.':___.'`.__.'`.__.':___.'`.__.':_;:_;`.__.':___.':___.'
    
        The following options are available:
    
        1 - List Servers	  8 - SSH into a server
        2 - Create Servers	  9 - Feature coming soon
        3 - Create Load Balancer  10 - Feature coming soon
        4 - Cloud Files		  11 - Feature coming soon
        5 - DNS Options		  12 - Feature coming soon
        6 - Databases
        7 - Backup
        """
    choice = raw_input("Please enter a command (h for help): ")
    if int(choice) == 1:
        print
        time.sleep(1)
	listservers()
	time.sleep(5)
	os.system('clear')	
    elif int(choice) == 2:
        print
	time.sleep(1)
	createservers()
	time.sleep(1)
	os.system('clear')
    elif int(choice) == 3:
	print
	time.sleep(1)
        print "Creating Load Balancer" # replace with function call
	time.sleep(1)
	os.system('clear')
    elif int(choice) == 4:
	print
	time.sleep(1)
        print "Cloud Files" # replace with function call
	time.sleep(1)
	os.system('clear')
    elif int(choice) == 5:
	print
	time.sleep(1)
        print "DNS Options" # replace with function call
	time.sleep(1)
	os.system('clear')
    elif int(choice) == 6:
	print
	time.sleep(1)
        print "Databases" # replace with function call
	time.sleep(1)
	os.system('clear')
    elif int(choice) == 7:
	print
	time.sleep(1)
        print "Backup" # replace with function call
	time.sleep(1)
	os.system('clear')
    elif int(choice) == 8:
        print
	time.sleep(1)
	connectServer()
        time.sleep(1)
	os.system('clear') 
    else:
	print
	time.sleep(1)
        print "Ivalid choice! Try again!"
	time.sleep(1)
	os.system('clear')
    return

os.system('clear')
while True:
    menu()
