#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:24:14 2022

@author: linuxlite

func for fetching ticker data, saving to db, fetching from db

todo: seperate the db , const++ per 100k rows, 
"""

import requests
from datetime import datetime
import sqlite3


class Stats:
    
    def __init__(self):
        '''
        create db, setup connection, create/not table 
        '''
        db_name='stats.db'    
        tb_name=str(datetime.now().strftime("tb_y%Y_m%m_d%d_%p"))
        
        self.tb_name=tb_name
        self.db_name=db_name
        
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.connection.cursor()
        print("Opened database successfully")
        self.connection.execute(f"CREATE TABLE IF NOT EXISTS {tb_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT,market TEXT NOT NULL, change_24_hour REAL NOT NULL, high, low, volume, last_price, bid,ask, timestamp);")       
        
        self.connection.commit()
        
    
    def db_init(self):
        
        
        pass
        
        
        #self.conn.close()

    
    
    
    
    def insertmany(self,tb_name,ex_data):
        
        #if table name doesnt come through, assume last  table. 
        #dangerous as no error thrown
        #assume tickr genration ongoing
        if tb_name=='':
            tb_name=self.tb_name
            print(f'Ticker saved to {tb_name}')
            
        q=f"INSERT INTO {tb_name} ( market,change_24_hour,high,low, volume, last_price, bid, ask, timestamp ) VALUES (?,?,?,?,?,?,?,?,?)"
        
        try:            
            self.cur.executemany(q, ex_data)
            self.connection.commit()
        except Exception as e:
            print(f'Couldnt process query: {q} for exdata: {ex_data}\nERR: {e}')
        
            
    
    
    
    
    
    
    
    def insert_in_tables(self,tb_name,data):
        '''
        data=( market,change_24_hour,high,low, volume, last_price, bid, ask, timestamp )
        '''
        ex_data=('market',data[0],data[1],data[2],data[3],data[4] ,data[5] ,data[6] ,data[7] )
        self.cur.execute(f"INSERT INTO {tb_name} ( market,change_24_hour,high,low, volume, last_price, bid, ask, timestamp ) VALUES (?,?,?,?,?,?,?,?,?)", ex_data )
        self.connection.commit()
    
    
    
    
    
    
    
    def search_in_tables(self,tb_name,col_name='',col_value=''):
        sorting_col='timestamp'
        #default ordering by timestamp, mostly desc 
        print(f'tb_name={tb_name}')
                
        if col_name and col_value:
            
            
            
            if tb_name=='all':
                #try:
                    
                q=self.cur.execute('SELECT name FROM sqlite_sequence')
                all_tbs=[tu[0] for tu in list(q)]
                print(f'all_tbs {all_tbs}')
                all_tbs.reverse()
                print(f'reversed all_tbs {all_tbs}')
                
                #look in the most recent tb only, if found do not check others:
                    
                    
                for each_tb in all_tbs:
                    print(f'search in table: {each_tb} \tin col: {col_name} for value: {col_value}')
                    
                    self.cur.execute(f'SELECT * FROM {each_tb} WHERE {col_name} is \'{col_value}\' ORDER BY {sorting_col} DESC LIMIT 1')
                    #getting a single row - the last one of the tb
                    
                    self.rows = self.cur.fetchall()     
                    if self.rows:
                        print('rows fetched successfully')
                        print(self.rows)
                        
                        with open ('op23432.txt','a+') as f:
                            f.write(str(self.rows))
                            f.write('\n\n')
                    
                #except Exception as e:
                    #print(f'Cant lookup table names due to error {e}')
                    
            else:
            #exact table name given, fetch all matching rows
                    
                print(f'search in table: {tb_name} \tin col: {col_name} for value: {col_value}')
                
                self.cur.execute(f'SELECT * FROM {tb_name} WHERE {col_name} is \'{col_value}\' ORDER BY {sorting_col} DESC')
                self.rows = self.cur.fetchall() 
                
                if self.rows:
                    print('rows fetched successfully')                   
                    return self.rows
                #print(self.rows)
        
        else:
            #print("no col name, col value given")
            self.cur.execute(f'SELECT * FROM {tb_name} ORDER BY {sorting_col} DESC')
            self.rows = self.cur.fetchall()
            if self.rows:
                print('rows fetched successfully')
            #return rows
            #print(self.rows)
            
        '''
        if self.rows:
            for row in self.rows:
                print(f'\nfound: {row}')
                print()'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    def get_ticker(self):
        pass
    
        '''
        self.exc=''
        #tickrfile="cryptodict.csv"
        params=["change_24_hour", "high", "low", "volume", "last_price", "bid", "ask","timestamp"]  
        url = "https://api.coindcx.com/exchange/ticker" # contains data about all the coins in  a single dict
        now = datetime.now()
        current_time = str(now.strftime("%I_%M%p"))
        try:
            response = requests.get(url)
            data = response.json()
            print("#\nurl accessed from get_ticker at "+current_time)
            #print(data)
    
        except Exception as e:
            print("Exception: ", e)
        
        #list of tuples . tuples have individual coin details
        #to push as SQL queries to db
        self.data_li=[]
        
        for coin in data:
            c=[]
            c.append(coin['market'])
            
            try:                
                for p in params:      
                    if p:
                        #print(coin[p])
                        c.append(coin[p])
                self.data_li.append(tuple(c))
                
            except Exception as e:
                print(f"Exception occured error while creating data_li: {e}")
                print(f'exc while processing {coin}')'''
                
            
        #print(self.data_li)
        
        
        
        
        
        
        
        
        # print(data)
        
        #write header
        '''with open(tickrfile,"a+") as f:
            f.write('market')
            f.write('\t')
            for p in params:
                f.write(p)
                f.write('\t') 
            f.write('\n')
        
        
        #write contents
        try:
            with open(tickrfile,"a+") as f:
                for coin in data: 
                    f.write(coin['market'])
                    f.write('\t') 
                    for p in params:                    
                        f.write(str(float(coin[p])))
                        f.write('\t')                     
                    f.write('\n')
            print(f"Ticker saved to {tickrfile}")
            
            
        except Exception as e:
            print(e)
            print(coin)'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=='__main__':      
    obj = Stats()
    #obj.get_ticker()
    #obj.db_init()
    obj.search_in_tables('all','market','DOGEINR')
    
    '''
    obj.db_init()
    
    ts=[(1,23,4,5,654,756,6,34,3433),(1,23,4,5,654,756,6,34,3433),(1,23,4,5,654,756,6,34,3433),(1,23,4,5,654,756,6,34,3433)]
    
    current_set=''
    with open('const','r') as f:                
        current_set=f.readline()
        
    tb_name='dataset'+current_set
    
    for t in ts:
        obj.insert_in_tables(tb_name, t)'''
