"""
Declan  Ritzenthaler, declanr@bu.edu

assignment 11, task 1, backtesting a trading strategy
"""


import pandas as pd

def create_bollinger_bands(df, window = 21, no_of_std = 1, column_name = ''):
    'calculates bollinger bands'
    
    if column_name == '':
        prices = df.iloc[: , 1]
    else:
        prices = df[column_name]
    
    df2 = pd.DataFrame(index=df['Date'])
    df2['Observation'] = prices
    
    df2 = df2.fillna(method='ffill')
    df2['RollingMean'] = df2['Observation'].rolling(window).mean()
    
    stdev = prices.rolling(window).std()
    
    df2['UpperBound'] = df2['RollingMean'] + no_of_std * stdev
    df2['LowerBound'] = df2['RollingMean'] - no_of_std * stdev

    return df2

def create_long_short_position(df):
    'calculates when to buy and when to sell'
    position = pd.DataFrame(index=df.index)
    signal = pd.Series(index = df.index, data = 0)
    
    for i in range(len(df)):
        if df['Observation'].iloc[i-1] > df['UpperBound'].iloc[i-1]:
            signal[i] = 1 # buy
        if df['Observation'].iloc[i-1] < df['LowerBound'].iloc[i-1]:
            signal[i] = -1 # sell
        
    position['Position'] = signal
        
    return position

def calculate_long_short_returns(df, position, column_name = ''):
    'calculates the returns based on whether we bought or sold'
    
    if column_name == '':
        prices = df.iloc[: , 1]
    else:
        prices = df[column_name]
    
    df2 = pd.DataFrame(index=df['Date'])
    
    long_returns = prices / prices.shift(1) - 1
    df2['Market Return'] = long_returns
    
    strategy_returns = position['Position'] * df2['Market Return']
    df2['Strategy Return'] = strategy_returns
    
    df2['Abnormal Return'] = df2['Strategy Return'] - df2['Market Return']
    
    return df2

def plot_cumulative_returns(df):
    'plots the cumulative returns'
    df[['Market Return', 'Strategy Return', 'Abnormal Return']].cumsum().plot()
    


if __name__ == '__main__':

    filename = './AAPL.csv'

    df = pd.read_csv(filename)
    df.index = df['Date']
    #df = df.loc['2015-01-01':'2020-12-31']
    bb = create_bollinger_bands(df, 50, 1, 'Adj Close')
    print(bb)
    bb.plot()

    position = create_long_short_position(bb)

    print(position)
    position.plot()
    
    returns = calculate_long_short_returns(df, position, 'Adj Close')
    print(returns)
    
    plot_cumulative_returns(returns)
    