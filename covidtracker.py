#!/usr/bin/python3

import time
import json
import sys
from urllib.request import Request, urlopen, HTTPError
from http.client import HTTPResponse, InvalidURL
from os import system, name 

def clear(): 
    #windows 
    if name == 'nt': 
        _ = system('cls') 
    #linux o mac
    else: 
        _ = system('clear')

def call_web(country):
    url = f"https://corona.lmao.ninja/v2/countries/{country}"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urlopen(req) as response:
            jsonResponse = json.load(response)

            print("{:^20s}|{:^17s}|{:^16s}|{:^16s}|{:^14s}|".format("Country","Confirmed Cases","Today Cases","Recovered","Deaths"))
            print("{:^20s}|{:^17d}|{:^16d}|{:^16d}|{:^14d}|".format(jsonResponse["country"],jsonResponse["cases"],jsonResponse["todayCases"],jsonResponse["recovered"],jsonResponse["deaths"]))
    except (HTTPError, InvalidURL) as err:
        print ("Something went wrong. Please check the Country name you introduced")
        sys.exit()

if __name__ == "__main__":
    #defaults to Argentina
    country = "Argentina"
    arguments = len(sys.argv) - 1
    if arguments > 0:
        #TODO encode parameter 
        country = sys.argv[1]


    call_web(country)
    while True:
        #long wait 6 hours
        time.sleep(21600)
        clear()
        call_web(country)
