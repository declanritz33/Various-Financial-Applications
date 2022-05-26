"""
Declan Ritzenthaler, declanr@bu.edu

Databases with SQL
"""

import sqlite3 as db
import pandas as pd

# set some options to display enough columns of output
pd.set_option('display.width', 320)
pd.set_option('display.max_columns',10)
    

# These queries will help you discover the database schema (structure).
example_0a = '''SELECT name FROM sqlite_master'''
example_0b = '''pragma table_info(clients)'''
example_0c = '''pragma table_info(trades)'''
example_0d = '''pragma table_info(price_history)'''


# This is an example query that you can use to get started:
## QUERY 00 SHOW ALL CLIENTS IN DATABASE
clients = '''
SELECT * 
FROM clients
'''

trades = '''
SELECT *
FROM trades
ORDER BY trade_date
'''

price_history = '''
SELECT *
FROM price_history
'''

sql_01 = '''
SELECT * FROM 
price_history WHERE date = '2020-12-31'
ORDER BY security
'''

sql_02 = '''
SELECT * FROM
trades WHERE client_id = 4
ORDER BY trade_date
'''

sql_03 = '''
SELECT * FROM
trades WHERE trade_date <= '2018-12-31' and trade_date >= '2018-01-01'
ORDER BY trade_date ASC
'''

sql_04 = '''
SELECT security, count(trade_date)
FROM trades
GROUP BY security
ORDER BY security
'''

sql_05 = '''
SELECT clients.first_name, clients.last_name, COUNT(trades.client_id)
FROM clients
INNER JOIN trades
    ON clients.client_id = trades.client_id
GROUP BY trades.client_id
ORDER BY COUNT(trades.client_id) DESC
'''

sql_06 = '''
SELECT clients.first_name, clients.last_name, trade_date, security, quantity
FROM trades
INNER JOIN clients
    ON clients.client_id = trades.client_id
WHERE security = 'CSCO'
ORDER BY trade_date ASC
'''

sql_07 = '''
SELECT clients.first_name, clients.last_name, trade_date, security, quantity
FROM trades
INNER JOIN clients
    ON clients.client_id = trades.client_id
WHERE trade_date <= '2019-12-31' and trade_date >= '2019-01-01'
ORDER BY trades.trade_date
'''

sql_08 = '''
SELECT trades.trade_date, trades.security, trades.quantity, price_history.price
FROM trades
INNER JOIN price_history
    ON price_history.date = trades.trade_date and price_history.security = trades.security
WHERE trades.client_id = 4
ORDER BY trades.trade_date ASC
'''

sql_09 = '''
SELECT trades.security, SUM(trades.quantity) as Quantity, price_history.price, price_history.price*Quantity as value
FROM trades
INNER JOIN price_history
    ON price_history.date = '2020-12-31' and price_history.security = trades.security
WHERE trades.client_id = 4 and price_history.date <= '2020-12-31'
GROUP BY trades.security

ORDER BY value DESC
'''


################################################################################
def run_query(sql):
    
    
    # obtain a database connection:
    con=db.connect("./portfolio.db")

    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    df = pd.read_sql(sql, con=con)

    return df


################################################################################
if __name__ == '__main__':
    
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    print(run_query(clients))
    print(run_query(trades))
    print(run_query(price_history))

    
    #print(run_query(sql_01))
    
    #print(run_query(sql_02))
    
    #print(run_query(sql_03))
    
    #print(run_query(sql_04))
    
    print(run_query(sql_05))
    
    #print(run_query(sql_06))
    
    #print(run_query(sql_07))
    
    #print(run_query(sql_08))

    print(run_query(sql_09))

