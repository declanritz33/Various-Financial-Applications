"""
Declan Ritzenthaler, declanr@bu.edu

assignment 11, Portfolio construction and rebalancing
"""

import pandas as pd
import math


def create_equal_weight_portfolio(df_prices, initial_value = 1):
    'shows price and portfolio value evoltuion'
    returns = pd.DataFrame(index = df_prices.index)
    
    for col in df_prices:
    
        returns[col] = df_prices[col] / df_prices[col].shift(1) - 1
    
    print(returns)
    print(df_prices[col].shift(0))
    
    weight = initial_value/len(df_prices.columns)
    
    values = pd.DataFrame(index = df_prices.index)
    
    
    
    for col in returns:
    
        values[col] = weight
        values[col] = values[col] * (math.e**returns[col])
    
        
    values['portfolio'] = values.sum(axis=1)
    
    returns = values / values.shift(1) - 1
    
    
    return values
    
    





if __name__ == '__main__':
    
    df = pd.read_csv('./AAPL.csv')
    df.index = df['Date']
    df2 = pd.read_csv('./NVDA (2).csv')
    df2.index = df2['Date']
    df3 = pd.read_csv('./GM.csv')
    df3.index = df3['Date']
    
    prices = pd.DataFrame()
    prices['AAPL'] = df['Adj Close']
    prices['NVDA'] = df2['Adj Close']
    prices['GM'] = df3['Adj Close']
    print(prices)
    
    values = create_equal_weight_portfolio(prices)
    print(values)
    print(values.describe())
    
    
    
    
    
    
    