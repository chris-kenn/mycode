#!/usr/bin/env python3
"""using csv data"""
import csv

def main():
    # open data
    with open("vendor.csv", "r") as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=",")
        # csv data is now a nice list
        for row in vendata:
            print("The IP address " + row[2] + \
                    " requires the driver " + row[3])

main()
