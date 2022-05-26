"""
Declan Ritzenthaler, declanr@bu.edu

assignment 12, task 2, quantifying investment risks, drawdown
"""

import pandas as pd
import numpy as np
from a9task1 import MCStockSimulator

def compute_drawdown(prices):
    'computes the drawdown prices data frame'
    drawdown = pd.DataFrame(index = prices.index)
    
    drawdown['price'] = prices
    
    drawdown['prev_max'] = drawdown['price'].rolling(len(prices),min_periods=1).max()
    
    drawdown['dd_dollars'] = drawdown['prev_max'] - drawdown['price']
    
    drawdown['dd_pct'] = (drawdown['prev_max'] - drawdown['price']) / drawdown['prev_max']
    
    return drawdown

def plot_drawdown(df):
    'plots the drawdown figures'
    plot1 = pd.DataFrame(index = df.index)
    plot1['price'] = df.iloc[:,0]
    plot1['prev_max'] = df.iloc[:,1]
    
    plot1.plot()
    
    plot2 = pd.DataFrame(index = df.index)
    plot2['dd_pct'] = df.iloc[:,3]
    
    plot2.plot()
    
def run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials):
    'gets drawdown figures for MC simulated trials'
    
    lst = []
    
    for i in range(num_trials):
    
        sim = MCStockSimulator(init_price, years, r, sigma, trial_size)
    
        df = pd.DataFrame()
        df['price'] = sim.generate_simulated_stock_values()
        df['drawdown'] = df['price'].rolling(len(df['price']),min_periods=1).max()
        df['dd_dollars'] = df['drawdown'] - df['price']
        df['dd_pct'] = df['dd_dollars']/df['drawdown']
        
        max_drawdown_pct = df['dd_pct'].max()
    
        lst.append(max_drawdown_pct)
        
    drawdown_trials = np.array(lst)
    
    drawdown_list = pd.Series(drawdown_trials)
    
    return drawdown_list
    
    
    


if __name__ == '__main__':
    
    df = pd.read_csv('./AAPL.csv')
    # set the 'Date' column as index
    df.index = df['Date']
    prices = pd.DataFrame(df['Adj Close'])
    print(prices)
    # compute drawdown for this one stock
    dd = compute_drawdown(prices)
    #print(dd) 
    plot_drawdown(dd)
    
    df = pd.read_csv('./AAPL.csv')
    df['ret'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))    
    trial_size = 252 # trading days/year
    init_price = float(df['Adj Close'].sample())
    
    r = df['ret'].mean() * trial_size
    
    sigma = df['ret'].std() * np.sqrt(trial_size)
    years = 10
    num_trials = 100
    max_dd = run_mc_drawdown_trials(init_price,  years, r, sigma, trial_size, num_trials)
    print(max_dd.describe())
    max_dd.hist()
    