#!/usr/bin/python3

import io
import time
import json
from urllib.request import Request, urlopen
from http.client import HTTPResponse
from os import system, name 

def clear(): 
    #windows 
    if name == 'nt': 
        _ = system('cls') 
    #linux o mac
    else: 
        _ = system('clear')

def call_web():
    req = Request('https://corona.lmao.ninja/countries/Argentina', headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as response:
        jsonResponse = json.load(response)

        print("{:^20s}|{:^16s}|{:^16s}|{:^16s}|{:^16s}|".format("Pais","Total Casos","Nuevos Casos","Recuperados","Fallecimientos"))
        print("{:^20s}|{:^16d}|{:^16d}|{:^16d}|{:^16d}|".format(jsonResponse["country"],jsonResponse["cases"],jsonResponse["todayCases"],jsonResponse["recovered"],jsonResponse["deaths"]))

clear()
call_web()
while True:
    #Espera larga para no cargar servidor 6 horas
    time.sleep(21600)
    clear()
    call_web()
