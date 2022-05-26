"""
Declan Ritzenthaler, declanr@bu.edu

assignment 12, Quantifying investment risks
"""

from scipy.stats import norm as norm
import pandas as pd
import math

def compute_model_var_pct(mu, sigma, x, n):
    'compute value at risk'    

    Z = norm.ppf(1-x)
    
    Var = mu*n + Z*sigma*math.sqrt(n)
    
    return Var

def compute_historical_var_pct(returns, x, n):
    'computes the value at risk interval based on historical returns'
    
    mu = float(returns.mean())
    sigma = float(returns.std())
    
    Z = norm.ppf(1-x)
    
    Var = mu*n + Z*sigma*math.sqrt(n)
    
    return Var

if __name__ == "__main__":
    
    Var = compute_model_var_pct(.0008, .01, .98, 10)
    #print(Var)
    
    df = pd.read_csv('./AAPL.csv')
    df.index = df['Date']
    
    df2 = pd.DataFrame(index = df.index)
    df2['Prices'] = df['Adj Close']
    
    #print(df2)
    
    returns = pd.DataFrame(index = df.index)
    long_returns = df2['Prices'] / df2['Prices'].shift(1) - 1
    returns['Returns'] = long_returns
    
    print(returns)
    
    print(compute_historical_var_pct(returns, .99, 7))
    
    
