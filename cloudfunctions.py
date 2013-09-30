#!/usr/bin/env python
import pyrax
import time
import os

pyrax.settings.set('identity_type', 'rackspace')
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)

cs = pyrax.cloudservers

def listservers():
    os.system('clear')
    print "Listing Servers:"
    print
    servers =  cs.servers.list()
    for i in servers:
        print i.name
 	print
os.system('clear')
