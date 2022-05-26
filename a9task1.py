"""
Declan Ritzenthaler, declanr@bu.edu

assignment 9, task 1, simulating stock returns
"""

import numpy as np
import matplotlib.pyplot as plt
import math

class MCStockSimulator:
    'this class defines a stock object whose price we will predict'
    
    def __init__(self, s, t, mu, sigma, nper_per_year):
        'constructor inititializes properties of the stock object'
        
        self.s = s
        self.t = t
        self.mu = mu
        self.sigma = sigma
        self.nper_per_year = nper_per_year
        
        "s: current asset price"
        "t: option maturity time in years"
        "mu: annualized avg. rate of return on the stock"
        "sigma: annualized standard deviation of returns on hte stock"
        "nper_per_year: number of return periods per year"
        
    def __repr__(self):
        'makes a string representation of the object'
        
        string_rep = f'MCStockSimulator (s = ${self.s}, t = {self.t} (years), mu = {self.mu}, sigma = {self.sigma}, nper_per_year = {self.nper_per_year}'
        
        return string_rep
    
    def generate_simulated_stock_returns(self):
        
        'generates a time-sries simulation of a stock returns over a given time period'

        lst = []
        
        time = int(self.t * self.nper_per_year)
        
        for i in range(time):
            
            dt = 1 / self.nper_per_year
            
            Z = np.random.normal()
            
            ira = (self.mu - (self.sigma**2 / 2)) * dt  
            irb = (Z * self.sigma * math.sqrt(dt))
            individual_return = ira + irb
            
            lst.append(individual_return)
            
        returns = np.array(lst)

        return returns
    
    def generate_simulated_stock_values(self):
        
        'generates a time-sries simulation of a stock price over a given time period'
        
        lst = [self.s]
        
        returns = MCStockSimulator.generate_simulated_stock_returns(self)
        
        
        for r in returns:
            lst.append(lst[-1] * (math.e**r))
                
        prices = np.array(lst)
            
        return prices
        
        #return prices
        
    def plot_simulated_stock_values(self, num_trials = 1):
        """ Generates a plot of of num_trials series of simulated stock returns.
        num_trials is an optional parameter; if it is not supplied, the default value of 1 will be used."""
        
        fig, ax = plt.subplots()
        ax.set_title(f'{num_trials} simulated trials')
        ax.set_xlabel('years')
        ax.set_ylabel('$ value')
        
        #x = np.arange(0,self.__t+.0001,self.__t/(self.__nper_per_year*self.__t))
        #y = prices
        
        #print(prices)

        for i in range(num_trials):
            
            prices = self.generate_simulated_stock_values()
            
            x = np.arange(0,self.t+.001,self.t/(self.nper_per_year*self.t))
            y = prices
        
            plt.plot(x, y)
            
        
        return 0
        
        
        
        
if __name__ == '__main__':        

    sim = MCStockSimulator(100, 1, 0.10, .30, 250)
    print(sim.generate_simulated_stock_returns())
    print(sim.generate_simulated_stock_values())
    print(sim.plot_simulated_stock_values(5))