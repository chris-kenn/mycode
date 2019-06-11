#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=2ZB3cgDnvByS0wkCB8QFPmI5Rrzc1DNE97F2b83t' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()
