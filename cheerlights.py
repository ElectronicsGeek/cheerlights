#!/usr/bin/python3

# cheerlights.py
# Code to abstract the Cheerlights API

import requests

class Cheerlights(object):
    
    def __init__(self):
        self.CL_NAME_URL = "http://api.thingspeak.com/channels/1417/field/1/last.json"
        self.CL_HEX_URL = "http://api.thingspeak.com/channels/1417/field/2/last.json"
        
    @property
    def last_color_name(self):
        r = requests.get(self.CL_NAME_URL)
        j = r.json()
        
        color = j['field1'] # Grab most recent color string from json
        
        return color
        
    @property
    def last_color_hex(self):
        r = requests.get(self.CL_HEX_URL)
        j = r.json()
        
        color = j['field2'] # # Grab most recent hex from json
        
        return color
        
    @property
    def last_color_rgb(self):
        # Remove the hex; leave a string of numbers.
        color = self.last_color_hex.strip("#")
        
        rgb_list = []
        for i in range(0,3):
            value = int(color[i:i+2],16)
            print value
            rgb_list.append(value)
            
        return rgb_list
