# CryptoNeeti
A package(in progress) to consume CoinDCX's API for Python, and provide a terminal interface to work with the data. The buy/sell backend hasn't been done yet. The values, however, are live.
Code Verbosity is intentionally for easier development.


# To use, just download the files, and do the following 3 steps:

# 1. The below line creates a database, 2 tables for each day: labelled as tb_y2022_m06_d12_PM indicating the year 2022, month 06, day 12 - PM. 
# you can then download the SQLite Browser if you simply want to see the values in the database. Or use the Charting.py module.
$ python Generate.py

# 2. Starts up a terminal to work with the data in sql. take note that user input only interacts with database and not with requests to api server. 
$ python terminal.py

# 3.(optional) If you want to see a graph of the live values
$ python Charting.py
