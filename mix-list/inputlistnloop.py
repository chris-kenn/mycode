#!/usr/bin/env python3

def main():
    # Read in data
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip: # single line in file from sline
            networklists.append(sline.rstrip("\n").split(' ' ))

    print(networklists) # display networklists
   
    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
