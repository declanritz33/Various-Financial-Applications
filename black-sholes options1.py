"""
Created on Thu May 26 13:30:26 2022

@author: Declan
"""
#Declan Ritzenthaler, declanr@bu.edu
#assignment 7, Black-Scholes option pricing model

"creating a class of Options, implementing methods to price and predict the option"

from scipy.stats import norm
import math

class BSOption:
    '''
    this class defines an European, non dividend paying option
    '''
    def __init__(self, s, x, t, sigma, rf, div):
        '''
        constructor initializes an object of type BSOption with the given parameters
        '''
        self.__s = s
        self.__x = x
        self.__t = t
        self.__sigma = sigma
        self.__rf = rf
        self.__div = div
        '''
        s = current price of underlying asset
        x = option strike price
        t = option matrutiy time(in years)
        sigma = annualized standard deviation of returns
        rf = annulaized risk free asset rate
        div = annualized dividend rate
        '''
        
    def __repr__(self):
        '''
        string representation of BSOption object
        '''
        string_rep = f's = ${self.__s}, x = ${self.__x}, t = {self.__t} (years), sigma = {self.__sigma}, rf = {100*self.__rf}%, div = {self.__div}'
        
        return string_rep
    
    def d1(self):
        'method calculates d1'
        numerator = (math.log(self.__s/self.__x)) + (self.__rf - self.__div + 0.5*self.__sigma**2)*self.__t
        denominator = self.__sigma * self.__t**0.5
        
        d1 = numerator/denominator
        
        return d1
    
    def d2(self):
        'method calculates d2'
        numerator = (math.log(self.__s/self.__x)) + (self.__rf - self.__div + 0.5*self.__sigma**2)*self.__t
        denominator = self.__sigma * self.__t**0.5
        
        d1 = numerator/denominator
        
        d2 = d1 - self.__sigma * self.__t**0.5
        
        return d2
    
    def nd1(self):
        'method calculates normal prob. dist. of d1'
        numerator = (math.log(self.__s/self.__x)) + (self.__rf - self.__div + 0.5*self.__sigma**2)*self.__t
        denominator = self.__sigma * self.__t**0.5
        
        d1 = numerator/denominator
        
        nd1 = norm.cdf(d1)
        
        return nd1
    
    def nd2(self):
        'method calculates normal prob. dist. of d2'
        numerator = (math.log(self.__s/self.__x)) + (self.__rf - self.__div + 0.5*self.__sigma**2)*self.__t
        denominator = self.__sigma * self.__t**0.5
        
        d1 = numerator/denominator
        
        d2 = d1 - self.__sigma * self.__t**0.5
        
        nd2 = norm.cdf(d2)
        
        return nd2
    
    def nd1_inverted(self):
        'method calculates normal prob. dist. of -d1'
        
        numerator = (math.log(self.__s/self.__x)) + (self.__rf - self.__div + 0.5*self.__sigma**2)*self.__t
        denominator = self.__sigma * self.__t**0.5
        
        d1 = numerator/denominator
        
        nd1_inverted = norm.cdf(-d1)
        
        return nd1_inverted
    
    def nd2_inverted(self):
        'method calculates normal probability dist. of -d2'
        
        numerator = (math.log(self.__s/self.__x)) + (self.__rf - self.__div + 0.5*self.__sigma**2)*self.__t
        denominator = self.__sigma * self.__t**0.5
        
        d1 = numerator/denominator
        
        d2 = d1 - self.__sigma * self.__t**0.5
        
        nd2_inverted = norm.cdf(-d2)
        
        return nd2_inverted
    
    def value(self):
        'value method for the base class, does not calculate anything'
        print("Cannot calculate value for base class BSOption")
        return 0
    
    def delta(self):
        'delta method for base class, does not calculate anything'
        print("Cannot calculate delta for base class BSOption")
        return 0
    
    def change_sigma(self,new_sigma):
        'changes the sigma'
        self.__sigma = new_sigma
    
    
class BSEuroCallOption(BSOption):
    '''
    BSEuroCallOption is a subclass of the BSOption class
    '''
    def __init__(self, s, x, t, sigma, rf, div):
        'constructor initializes the same parameters as its parent class'
        self.__s = s
        self.__x = x
        self.__t = t
        self.__sigma = sigma
        self.__rf = rf
        self.__div = div
        '''
        s = current price of underlying asset
        x = option strike price
        t = option matrutiy time(in years)
        sigma = annualized standard deviation of returns
        rf = annulaized risk free asset rate
        div = annualized dividend rate
        '''
        BSOption.__init__(self, s, x, t, sigma, rf, div)
        
    def value(self):
        'calculates the value of a European Call Option'
        
        from math import e
        Nd1 = BSOption.nd1(self)
        Nd2 = BSOption.nd2(self)
        
        value = (self.__s * e**(-self.__div * self.__t) * Nd1) - (self.__x * e**(-self.__rf * self.__t) * Nd2)
        
        return value
    
    def __repr__(self):
        'string rep for BSEuro Call Option'
        value = BSEuroCallOption.value(self)
        
        string_rep = f'BSEuroCallOption, value = ${value:.2f} \nparameters: s = ${self.__s}, x = ${self.__x}, t = {self.__t} (years), sigma = {self.__sigma}, rf = {100*self.__rf}%, div = {self.__div}'
         
        return string_rep
    
    def delta(self):
        'calculates the delta of an option'
        
        from math import e
        
        Nd1 = BSOption.nd1(self)
        
        delta = e**(-self.__div * self.__t) * Nd1
        
        return delta
    
    
    
class BSEuroPutOption(BSOption):
    '''
    BSEuroPutOption is a subclass of the BSOption class
    '''    
    def __init__(self, s, x, t, sigma, rf, div):
        'constructor initializes the same parameters as its parent class'
        self.__s = s
        self.__x = x
        self.__t = t
        self.__sigma = sigma
        self.__rf = rf
        self.__div = div
        '''
        s = current price of underlying asset
        x = option strike price
        t = option matrutiy time(in years)
        sigma = annualized standard deviation of returns
        rf = annulaized risk free asset rate
        div = annualized dividend rate
        '''
        BSOption.__init__(self, s, x, t, sigma, rf, div)
        
    def value(self):
        'calculates the value of a European put option'
        
        from math import e
        
        Nd1_inv = BSOption.nd1_inverted(self)
        Nd2_inv = BSOption.nd2_inverted(self)
        
        value = (self.__x * e**(-self.__rf * self.__t) * Nd2_inv) - (self.__s * e**(-self.__div * self.__t) * Nd1_inv)
        
        return value
        
        
    def __repr__(self):
        'string rep for BSEuro Put Option'
        value = BSEuroPutOption.value(self)
        
        string_rep = f'BSEuroPutOption, value = ${value:.2f} \nparameters: s = ${self.__s}, x = ${self.__x}, t = {self.__t} (years), sigma = {self.__sigma}, rf = {100*self.__rf}%, div = {self.__div}'
        
        return string_rep
    
    def delta(self):
        'calculates delta of a put option'
        
        from math import e
        
        Nd1_inv = BSOption.nd1_inverted(self)
        
        delta = -e**(-self.__div * self.__t) * Nd1_inv
        
        return delta
    

####
##unit test code

if __name__ == '__main__':
    
    call = BSEuroCallOption(100, 100, 1.0, 0.3, 0.06, 0.00)

    print(call.value())

    put = BSEuroPutOption(100, 100, 0.5, 0.5, 0.04, 0.02)
    print(put.delta())


######end of unit test code
