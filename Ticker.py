#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:26:17 2022

@author: linuxlite
"""

from datetime import datetime
import requests


class ticker:
    
    def __init__(self):     
        #get current ticker
        self.params=["change_24_hour", "high", "low", "volume", "last_price", "bid", "ask","timestamp"]  
        url = "https://api.coindcx.com/exchange/ticker" # contains data about all the coins in  a single dict
        now = datetime.now()
        current_time = str(now.strftime("%I_%M%p"))
        try:
            response = requests.get(url)
            self.data = response.json()
            print(f"# got new ticker value at : {current_time} (your machine time)")
            #print(data)
    
        except Exception as e:
            print("Exception: ", e)
    
    
    def get(self):
        '''
        generates the data_li list which hold current ticker value
        used by generate module to push to db
        '''
        #list of tuples . tuples have individual coin details
        #to push as SQL queries to db from another class       
        self.data_li=[]
        
        for coin in self.data:
            c=[]
            c.append(coin['market'])
            
            try:                
                for p in self.params:      
                    if p:
                        #print(coin[p])
                        c.append(coin[p])
                self.data_li.append(tuple(c))
                
            except Exception as e:
                print(f"Exception occured error while creating data_li: {e}")
                print(f'exc while processing {coin}')
                
        return self.data_li
        
