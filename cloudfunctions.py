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
    servers = cs.servers.list()
    for i in servers:
	print "Server: %s - IP: %s" % (i.name, i.accessIPv4)
 	print

def createservers(): # Fix this up so you can choose an image other than ubuntu
    os.system('clear')
    servers = {} # REMOVE
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
    cs.servers.create(base_name, image.id, flavor.id)
    # Create the servers
#    print "Requesting " + str(count) + " Ubuntu 12.04 512MB servers"
#    for i in xrange(0, count):
#        name = '%s%s' % (base_name, i)
#        servers[name] = cs.servers.create(name, ubu_image.id, flavor_512.id)

def connectServer(): #TODO: Clean this up and make more awesome
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
    user = 'root@'
    connection = user + ip
    os.execlp('ssh', 'ssh', connection)

