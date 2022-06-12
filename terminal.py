#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:30:20 2022

@author: linuxlite

user terminal
"""

from DBase import Stats
from datetime import datetime
import time


class Term_main:
    
    def start(self):
        
        self.flag=True
        
        while self.flag:            
            
            self.ip=input("\n>> ")     
            self.command_dispatcher(self.ip)            
            
            
    
    def command_dispatcher(self,ip):
        print("\nYou've entered: ", ip) 
        commands={'exit':['exit','0'], 'help': ['help','h'] , 'searchcoin': ['find','compare','f'], 'findlive':['findlive','fl'] , 'show': ['show','sh']}
        
        #single word commands
        if ip.casefold() in commands['exit']:
            self.flag=False
            print('Thank you for using ...')
        
        elif ip.casefold() in commands['help']:
            s=f'Commands available: {commands}'
            print(s)
            
        else:
            #multi word commands and flags...
            ip_li=ip.casefold().split(' ')
            print(f'iusre input listified:   {ip_li}')
            
            
            if ip_li[0] in commands['show']:
                #visualizations, charts
                coinname=ip_li[1]
                
                import chh
                
                obj = chh()
                
            
            if ip_li[0] in commands['findlive']:
                #repeating values every 30 secs
                #find only the most latest value
                
                coinname=ip_li[1]
                dbobj = Stats()
                
                while True:   
                    client_t=datetime.now().strftime('%a, %d-%h-%Y %-I%p %Mmins %Ssecs')
                    print(f'\n#####Your timee: {client_t}')
                    tb_name=str(datetime.now().strftime("tb_y%Y_m%m_d%d_%p"))
                    
                    searchtup=dbobj.search_in_tables(tb_name, 'market', coinname.upper())
                    #print((searchtup[0])[-1])
                    ts=(searchtup[0])[-1]
                    dt_obj = datetime.fromtimestamp(ts)
                    
                    dt_= dt_obj.strftime('%a, %d-%h-%Y %-I%p %Mmins %Ssecs')
                    print(f'\t: {searchtup[0]} \nfor remote server time: {dt_}')
                                        
                    '''
                    st=input('type 0(zero) to stop. enter to continue: ')
                    start_t=datetime.now().timestamp()
                    print(f'start_t={start_t}')
                    
                    current_t=datetime.now().timestamp()
                    
                    diff=current_t-start_t
                    print(f'diff={diff}')
                    
                        
                    current_t=datetime.now().timestamp()
                    diff=current_t-start_t'''
                    
                    
                        
                    #print('continuing...')
                    print('Sleeping for 30 secs...')
                    time.sleep(30)
                    
                
                
                
            if ip_li[0] in commands['searchcoin']:
                
                coinname=ip_li[1]
                
                obj = Stats()
                obj.db_init()
                
                current_set=''
                with open('const','r') as f:                
                    current_set=f.readline()
                                    
                tb_name=f'dataset{current_set}'
                
                obj.search_in_tables(tb_name, 'market', coinname.upper())
                
                rows=obj.rows
                
                for row in rows:
                    
                    dt_= datetime.fromtimestamp(row[-1]).strftime('%a, %d-%h-%Y %-I%p %Mmins %Ssecs')
                    print(f'row: {row} at {dt_}')                    
                    break
                
    
            
if __name__=='__main__':
    Terminal=Term_main()
    Terminal.start()
