#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:11:41 2022

@author: linuxlite

Generates the ticker in DB every 30 secs


"""


import time 
from DBase import Stats
from Ticker import ticker


class Generate:
    
    def tick():
        sv=0
        while True:
            sv+=1
            print(f'\n\nsave #{sv}')

            dbobj = Stats()                  
            tk=ticker()                                      
            
            dbobj.insertmany('', tk.get())            
            dbobj.connection.close()
            
            print('sleeping for 29 secs...')
            time.sleep(29)
            
            
    
    

if __name__=='__main__':
    Generate.tick()
