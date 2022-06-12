# CryptoNeeti
A package(in progress) to consume CoinDCX's API for Python, and provide a terminal interface to work with the data. The buy/sell backend hasn't been done yet. The values, however, are live.
Code Verbosity is intentionally for easier development.


# To use, just download the files, and do :

$ python Generate.py
#the above line creates a database, creates 2 tables for each day. labeled as tb_y2022_m06_d12_PM indicating the year 2022, month 06, day 12 - PM. 
# you can then download the SQLite Browser if you simply want to see the values in the database

$ python terminal.py
# starts up a terminal to work with the data in sql. take note that user input only interacts with database and not with requests to api server. 

$ python Charting.py
# If you want to see a graph of the live values
