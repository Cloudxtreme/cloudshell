#!/usr/bin/env python

import pyrax
from cloudfunctions import listservers
import os
import time

def menu():
    print """
    Welcome to CloudShell v1.0
    
     .--. .-.    .--. .-..-..---.  .--. .-..-. .--. .-.   .-.   
    : .--': :   : ,. :: :: :: .  :: .--': :; :: .--': :   : :   
    : :   : :   : :: :: :: :: :: :`. `. :    :: `;  : :   : :   
    : :__ : :__ : :; :: :; :: :; : _`, :: :: :: :__ : :__ : :__ 
    `.__.':___.'`.__.'`.__.':___.'`.__.':_;:_;`.__.':___.':___.'
    
        The following options are available:
    
        1 - List Servers
        2 - Create Servers
        3 - Create Load Balancer
        4 - Cloud Files
        5 - DNS Options
        6 - Databases
        7 - Backup
        """
    choice = raw_input("Please enter a command (h for help): ")
    if int(choice) == 1:
        print
        time.sleep(1)
	listservers()
	time.sleep(1)
	os.system('clear')	

    elif int(choice) == 2:
        print "Creating servers"
    elif int(choice) == 3:
        print "Creating Load Balancer"
    elif int(choice) == 4:
        print "Cloud Files"
    elif int(choice) == 5:
        print "DNS Options"
    elif int(choice) == 6:
        print "Databases"
    elif int(choice) == 7:
        print "Backup"
    else:
        print "Ivalid choice! Try again!"
    return

os.system('clear')
while True:
    menu()