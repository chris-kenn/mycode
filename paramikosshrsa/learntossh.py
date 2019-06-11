#!/usr/bin/env python3

import paramiko
import os

def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, sshstderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()


sshsession = paramiko.SSHClient()

# user/pass connection

# sshsession.connect(server, username=username, password=password)
#

# using keys

mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

# Add fingerprint if needed
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Creds
#ip_name = input('Enter the IP of the host you wish to connect to or enter done if finished: ')
#if ip_name != 'done':
#    user = input('Enter the username: ')
#    shsession.connect(hostname=ip_name, username=user, pkey=mykey)  







sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

# various commands
# our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]
command = "a"
our_commands = []


while command:
    command = input('Enter commands you would like to run: ' ) 
    our_commands.append(command)


for x in our_commands:
    print(commandissue(x).decode('utf-8'))


