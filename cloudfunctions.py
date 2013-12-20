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
    print "Listing Servers in DFW region:"
    print "=============================="
    servers_dfw = cs.servers.list()
    if servers_dfw:
        for i in servers_dfw:
            print "Server: %s - IP: %s" % (i.name, i.accessIPv4)
   	    print
    else:
        print "No servers found in DFW"

    print "Listing Servers in IAD region:"
    print "=============================="
    cs_iad = pyrax.connect_to_cloudservers(region="IAD")
    servers_iad = cs_iad.servers.list()
    if servers_iad:
        for i in servers_iad:
            print "Server: %s - IP: %s" % (i.name, i.accessIPv4)
            print
    else:
        print "No servers found in IAD region"
        print

    print "Listing servers in ORD region:"
    print "=============================="
    cs_ord = pyrax.connect_to_cloudservers(region="ORD")
    servers_ord = cs_ord.servers.list()
    if servers_ord:
        for i in servers_ord:
            print "Server: %s - IP: %s" % (i.name, i.accessIPv4)
            print
    else:
        print "No servers found in ORD region"
        print

def createservers():
    os.system('clear')
    servers = {}
    images = cs.images.list()
    for pos, img in enumerate(images):
        pos += 1
        print "%s - %s" % (pos, img.name)
    choice = int(raw_input("Which image would you like to use: "))
    choice -= 1
    image = images[choice]
    print "You picked %s now choose a flavor: " % image.name
    flavors = cs.flavors.list()
    for pos, fla in enumerate(flavors):
        pos += 1
        print "%s - %s" % (pos, fla.name)
    choice = int(raw_input("Enter the number of the flavor you want: "))
    choice -= 1
    flavor = flavors[choice]
    count = int(raw_input("Enter the number of servers you want to create: "))
    base_name = raw_input("Enter a base name for the server: ")
    print "Creating %s %s servers with %s flavor" % (count, image.name, flavor.name)
    time.sleep(5)
    for i in xrange(0, count):
	i += 1
        name = '%s%s' % (base_name, i)
        servers[name] = cs.servers.create(name, image.id, flavor.id)
    
def connectServer():
    os.system('clear')
    print "Choose a server to connect to:"
    servers = cs.servers.list()
    for pos, server in enumerate(servers):
        pos += 1
        print "%s: %s" % (pos, server.name)
    choice = int(raw_input("Enter a number: "))
    choice -= 1
    server = servers[choice]
    print "Connecting to  %s " % server.name
    ip = servers[choice].accessIPv4
    user = raw_input("Username: ")
    connection = user + '@' + ip
    os.execlp('ssh', 'ssh', connection)

