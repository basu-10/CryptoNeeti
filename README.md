# CryptoNeeti
A package(in progress) to consume CoinDCX's API for Python, and provide a terminal interface to work with the data. The buy/sell backend hasn't been done yet. The values, however, are live.
Code Verbosity is intentionally for easier development.


### To use, just download the files, and do the following 3 steps:

### 1. The below line creates a database called *stats.db*, 2 tables for each day: labelled as *tb_y2022_m06_d12_PM* indicating the *y*ear *2022*, *m*onth *06*, *d*ay *12* - *PM*. 
```
$ python Generate.py
```

> To see the values in the database ,you can use the DB Browser for SQLite: https://sqlitebrowser.org. 

> Or, in step2., use the interactive prompt to see live coin values and compare coin values using simple commands like *find*,*compare*,*findlive*.
> Or, in step3.(optional), use the *Charting.py* module to see live coin values.

### 2. Starts up a terminal to work with the data in sql. take note that user input only interacts with database and not with requests to api server. 
```
$ python terminal.py
```

### 3.(optional) If you want to see a graph of the live values
```
$ python Charting.py
```
> *Generate.py* must be kept open to get the live values at 30s intervals, based on CoinDCX's ticker time(values refreshed after every 30s).
