#!/usr/bin/env python
import pyrax
import time
import os
import re

pyrax.settings.set('identity_type', 'rackspace')
creds_file = os.path.expanduser("~/.rackspace_creds")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

# Basic listing of servers
def listservers():
    os.system('clear')
    print "Listing Servers:"
    print "=============================="
    servers = cs.servers.list()
    if servers:
        for i in servers:
            print "Server: %s - IP: %s" % (i.name, i.accessIPv4)
   	    print
        raw_input("Press any key to return to main menu")
        return
    else:
        print "No severs found in %s region" % region

# Create one or more servers
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
    # Get SSH key TODO: WARN if does not exist
    content = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
    sshkey = {"/root/.ssh/authorized_keys": content}
    if count == 1:
	name = base_name
        servers[name] = cs.servers.create(name, image.id, flavor.id, files=sshkey)
    else:
        for i in xrange(0, count):
	    i += 1
            name = '%s%s' % (base_name, i)
            servers[name] = cs.servers.create(name, image.id, flavor.id, files=sshkey)

# open SSH connection    
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

# add a host to ansible server
def ansibleAdd():
    os.system('clear')
    print "Choose a server to add to the Ansible master host: "
    servers = cs.servers.list()
    for pos, server in enumerate(servers):
        pos += 1
        print "%s: %s" % (pos, server.name)
    choice = int(raw_input("Enter a number: "))
    choice -= 1
    server = servers[choice]
    hostentry = "%s %s\n" % (server.accessIPv4, server.name)
    print hostentry
    print "Creating /etc/hosts entry for %s" % server.name
    with open("/etc/hosts", "a") as hostsfile:
        hostsfile.write(hostentry)
    ansiblehost = server.name
    ansiblegroup = raw_input("What group do you want to add the ansible node to: ")
    with open('/etc/ansible/hosts', 'r+') as searchfile:
        for line in searchfile:
            if re.search('\[' + ansiblegroup + '\]', line, re.M|re.I):
                print "%s exists" % ansiblegroup
            else:
                print "%s group does not exist" % ansiblegroup

#    print "Adding %s to /etc/ansible/hosts as part of the %s group: " % (ansiblehost, ansiblegroup) #TODO: FIX THIS
#    for line in reversed(open("/etc/ansible/hosts").readlines()):
#        if line.rstrip().endswith(ansiblegroup):
#            with open("/etc/ansible/hosts", "a") as anshostfile:
#                anshostfile.write(ansiblegroup + "\n" + ansiblehost) #TODO: FIX
#    else:
#        with open("/etc/ansible/hosts", "a") as anshostfile:
#            anshostfile.write("\n" + ansiblegroup + "\n")
#            anshostfile.write(ansiblehost + "\n")
    raw_input("Press any key to continue: ")


