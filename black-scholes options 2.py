
#Declan Ritzenthaler, declanr@bu.edu
#assignment 7, Black-Scholes Option Pricing Model

'generating a table of option charactersitics given price changes, finding implied volatility'

from a7task1 import *

def generate_option_value_table(s, x, t, sigma, rf, div):
    
    'generates a table of changing call/put prices given changes in stock price'
    
    call = BSEuroCallOption(s, x, t, sigma, rf, div)
    put = BSEuroPutOption(s, x, t, sigma, rf, div)
    
    print(call)
    print(put, "\n")
    
    upper = s + 10
    lower = s - 10
    
    test_price = lower - 1
    
    print("   price  ",  "call value  ", "put value  ", "call delta  ", "put delta    ")
    
    while test_price < upper:
        
        test_price += 1
        
        call_value = BSEuroCallOption(test_price, x, t, sigma, rf, div).value()
        
        put_value = BSEuroPutOption(test_price, x, t, sigma, rf, div).value()
        
        call_delta = BSEuroCallOption(test_price, x, t, sigma, rf, div).delta()
        
        put_delta = BSEuroPutOption(test_price, x, t, sigma, rf, div).delta()
        
        print("${:7.2f}".format(test_price),"\t", 
              "${:6.2f}".format(call_value),"\t", 
              "${:6.2f}".format(put_value),"\t",
              "{:5.4f}".format(call_delta),"\t",
              "{:5.4f}".format(put_delta))
        
        

def calculate_implied_volatility(option, value):
    'calculates the implied volatility by iterating through different values while changing sigma'
    
    r0 = 0
    r1 = 1
    
    accuracy = .00001

    error1 = 1
    
    while (abs(error1)>accuracy):
        test_sigma = (r0+r1)/2
        if type(option) == BSEuroCallOption:
            option.change_sigma(test_sigma)
            test_value = BSEuroCallOption.value(option)
        else:
            option.change_sigma(test_sigma)
            test_value = BSEuroPutOption.value(option)
        error1 = test_value - value
        if test_value>value:
            r1 = test_sigma
        else:
            r0 = test_sigma
        print('test_sigma = %.8f, value = %.6f, diff = %.6f' %(test_sigma,test_value,error1))
    return test_sigma  


###unit test code

if __name__ == 'main':

    generate_option_value_table(100, 100, 0.5, 0.25, 0.04, 0.02)

    put= BSEuroPutOption(92.76, 90, 100/365, 0.5, 0.01, 0.00)

    print(calculate_implied_volatility(put,7.40))


####end of unit test code
