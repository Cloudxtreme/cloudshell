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
        print "Server: %s - IP: %s" % (i.name, i.accessIPv4)
 	print

def createservers():
    os.system('clear')
    servers = {}
    # We want Ubuntu 12.04 image and 512 slice
    ubu_image = [img for img in cs.images.list()
                    if "12.04" in img.name][0]
    print("Ubuntu Image:"), ubu_image
    flavor_512 = [flavor for flavor in cs.flavors.list()
                    if flavor.ram == 512][0]
    print("512 Flavor:"), flavor_512
    count = int(raw_input("Enter the number of servers you want to create: "))
    base_name = raw_input("Enter a base name for the server: ")
    # Create the servers
    print "Requesting " + str(count) + " Ubuntu 12.04 512MB servers"
    for i in xrange(0, count):
        name = '%s%s' % (base_name, i)
        servers[name] = cs.servers.create(name, ubu_image.id, flavor_512.id)

def connectServer():
    os.system('clear')
    print "Choose a server to connect to:"
    print
    x = 1
    servers = cs.servers.list()
    for i in servers:
        print x, i.name
        x += 1
    selection = int(raw_input("Please choose a server: "))    


#process = subprocess.Popen("ssh example.com ls", shell=True,
#    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#output,stderr = process.communicate()
#status = process.poll()
#print output
