
#Declan Ritzenthaler, declanr@bu.edu
#assignment 5, task 2: bond portfolio class

from a3task1 import *
from a5task1 import *

class BondPortfolio:
    '''
    creates a class of BondPortfolio objects
    '''
    def __init__(self):
        'constructor initiates an empty list as the object of type portfolio'
        self.__portfolio = []
        
    def __repr__(self):
        'outputs a string representation of the object and its attributes'
        #print('BondPortfolio contains' , len(self.__portfolio), 'bonds: ')
        BondString = ""
        for i in (self.__portfolio):
            BondString += f'{i}\n'
        return f'BondPortfolio contains {len(self.__portfolio)} Bonds: \n' + BondString + f'Portfolio value: ${BondPortfolio.get_value(self):.2f}\nPortfolio yield to maturity: {100*BondPortfolio.get_yield_to_maturity(self):.4f}%\nPortfolio Duration: {BondPortfolio.get_duration(self):.3f}\nPortfolio Convexity: {BondPortfolio.get_convexity(self):.3f}'
        
        #return f'{i}'
    def add_bond(self, b):
        'allows user to add attributes(bonds) to the object(portfolio)'
        self.__portfolio.append(b)
        
    def rem_bond(self,b):
        'allows user to remove bonds from the object(portfolio)'
        self.__portfolio.remove(b)

    def get_value(self):
        
        'allows user to extract the value of the bonds(attributes) in the portfolio(object)'
        prices = []
        for i in self.__portfolio:
            prices.append(i.get_price())
        
        return sum(prices)
    
    def get_yield_to_maturity(self):
        'allows user to extract the porfolio ytm'
        prices = []
        for i in self.__portfolio:
            prices.append(i.get_price())
        
        ytms = []
        for i in self.__portfolio:
            ytms.append(i.get_yield_to_maturity())
            
        pricesweighted = [i /sum(prices) for i in prices]
        
        weightedytms = [a * b for a , b in zip(ytms , pricesweighted)]
        
        weightedytm = sum(weightedytms)
        
        return weightedytm
    
    def get_duration(self):
        'allows user to extract the duration of the portfolio'
        prices = []
        for i in self.__portfolio:
            prices.append(i.get_price())
        pricesweighted = [i /sum(prices) for i in prices]    
        
        durations = []
        for i in self.__portfolio:
            durations.append(i.get_duration())
        
        d = [a * b for a , b in zip(durations,pricesweighted)]
        
        weighted_duration = sum(d)
        
        return weighted_duration
    
    def get_convexity(self):
        'allows user to extract the convexity of the portfolio'
        prices = []
        for i in self.__portfolio:
            prices.append(i.get_price())
        pricesweighted = [i / sum(prices) for i in prices]
        
        convexities = []
        for i in self.__portfolio:
            convexities.append(i.get_convexity())
            
        c = [a * b for a , b in zip(pricesweighted,convexities)]

        weighted_convexity = sum(c)

        return weighted_convexity

    def shift_ytm(self, delta_ytm):
        'allows a user to change the effective ytm by a fixed amount for all bonds in the portfolio'        
        for i in self.__portfolio:
            ytm = (i.get_yield_to_maturity() + delta_ytm)
            i.set_yield_to_maturity(ytm)


if __name__ ==  "__main__":
            
    bp = BondPortfolio()

    b1 = Bond(10000, 2, 0.06)
    b1.set_yield_to_maturity(.07)
    bp.add_bond(b1)
    
    b2 = Bond(10000, 5, .08)
    b2.set_yield_to_maturity(0.09)
    bp.add_bond(b2)
    
    b3 = Bond(5000, 10) # 10-year zero-coupon bond
    b3.set_yield_to_maturity(0.10)
    bp.add_bond(b3)
    print(bp)
    #bp.shift_ytm(.01)


    #print(bp)
