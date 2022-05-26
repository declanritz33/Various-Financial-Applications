'''
Declan Ritzenthaler, declanr@bu.edu

assignment #5 task 1, A bond class

'''
import math
from a3task1 import *


class Bond:
    '''
    creates a class of bond types
    '''
    def __init__(self, maturity_value, maturity_time, 
                  coupon_rate = 0, coupon_frequency = 2):
        '''
        constructor initializes an object of type Bond
        '''
     
        self.__maturity_value = maturity_value
        self.__maturity_time = maturity_time
        self.__coupon_rate = coupon_rate
        self.__coupon_frequency = coupon_frequency
        self.__price = maturity_value
        self.__yield_to_maturity = coupon_rate
        
    def __repr__(self):
        '''
        returns a string representation of Bond object
        '''
        string_rep = f'${self.__maturity_value:.2f} maturity, {self.__maturity_time}-year, {100*self.__coupon_rate:.3f}% bond, price = ${self.__price:.2f}, ytm = {100*self.__yield_to_maturity:.3f}%, duration = {Bond.get_duration(self):.4f}, convexity = {Bond.get_convexity(self):.4f}'
        return string_rep
    
    def get_maturity_value(self):
        'allows user to extract maturity value of bond object'
        return self.__maturity_value
    
    def get_maturity_time(self):
        'allows user to extract matruity time of bond object'
        return self.__maturity_time
    
    def get_coupon_frequency(self):
        'allows user to extract coupon frequency of bond object'
        return self.__coupon_frequency
    
    def get_coupon_rate(self):
        'allows user to extract coupon rate of bond object'
        return self.__coupon_rate
    
    def get_price(self):
        'allows user to extract price of bond object'
        return self.__price
    
    def get_coupon_amount(self):
        'allows user to extract coupon payment of bond object'
        amnt = (self.__price * self.__coupon_rate) / self.__coupon_frequency
        return amnt
    
    def get_yield_to_maturity(self):
        'allows user to extract yield to maturity of a bond object'
        return self.__yield_to_maturity
    
    def get_pmt_times(self):
        'allows user to extract payment times of bond object'
        n = self.__maturity_time
        m = self.__coupon_frequency
        pmt_times = [i+1 for i in range(n*m)]
    
        return pmt_times
    
    def get_cashflows(self):
        'allows user to extract cashflows of bond object'
        fv = self.__maturity_value
        c = self.__coupon_rate
        n = self.__maturity_time
        m = self.__coupon_frequency
        list1 = []
        coupon = (c/m)*fv
        total_coupons = int(n*m)
        final_payment = coupon + fv
        list1 = [coupon]*(total_coupons-1)
        list1.append(final_payment)
    
        return list1
    

    def get_discount_factors(self):
        'allows user to extract discount factors of bond object'
        r = self.__yield_to_maturity
        n = self.__maturity_time
        m = self.__coupon_frequency
        list_discount = [math.pow(1/(1+r/m) , i + 1) for i in range (n*m)]
    
        return list_discount
        
    def set_yield_to_maturity(self, new_ytm):
        'allows user to change hidden attribute yield_to_maturity'
        self.__yield_to_maturity = new_ytm
        def calculate_price(self):
            'calculates new price given a new ytm'
            fv = self.__maturity_value
            c = self.__coupon_rate
            r = self.__yield_to_maturity
            n = self.__maturity_time
            m = self.__coupon_frequency
            'calculating cashflows with new ytm'
            list1 = []
            coupon = (c/m)*fv
            total_coupons = int(n*m)
            final_payment = coupon + fv
            list1 = [coupon]*(total_coupons-1)
            list1.append(final_payment)
            'calculating discount factors with new ytm'
            list_discount = [math.pow(1/(1+r/m) , i + 1) for i in range (n*m)]
            'calculating bond price with new ytm'
            list_discounted_cashflows = [a * b for a, b in zip(list1, list_discount)]
            new_price = (sum(list_discounted_cashflows))
            self.__price = new_price
    
        calculate_price(self)
        
    def set_price(self, price):
        'allows user to set a price for the bond object'
        self.__price = price
        def calculate_yield_to_maturity(self, accuracy = .00001):
            'calculates the new ytm given the price'
            fv = self.__maturity_value
            c = self.__coupon_rate
            r = self.__yield_to_maturity
            n = self.__maturity_time
            m = self.__coupon_frequency
            r0 = -1
            r1 = 1

            error1 = 1
    
            test_rate = 1
    
            while(abs(error1)>accuracy):
                test_rate = (r0+r1)/2
                test_price = bond_price(fv,c,n,m,test_rate)
                error1 = test_price - price
                if test_price<price:
                    r1 = test_rate
                else:
                    r0 = test_rate
       
            self.__yield_to_maturity = test_rate  
                
                
            
        calculate_yield_to_maturity(self)
        
    def get_duration(self):
        "calculates duration given the bond obejct's parameters"
        fv = self.__maturity_value
        c = self.__coupon_rate
        r = self.__yield_to_maturity
        n = self.__maturity_time
        m = self.__coupon_frequency
        
        listcashflows = bond_cashflows(fv,c,n,m)
    
        listdiscountfactors = discount_factors(r, n, m)
    
        PVcashflows = [a * b for a, b in zip(listcashflows,listdiscountfactors)]
    
        listpaymenttimes = cashflow_times(n,m)
    
        dollar_years = [a * b for a, b in zip(PVcashflows, listpaymenttimes)]
    
        duration = (sum(dollar_years)/bond_price(fv,c,n,m,r))/2
        
        return duration
    
    def get_convexity(self):
        "calculates convexity given the bond object's parameters"
        fv = self.__maturity_value
        c = self.__coupon_rate
        r = self.__yield_to_maturity
        n = self.__maturity_time
        m = self.__coupon_frequency
        
        listcashflows = bond_cashflows(fv,c,n,m)
    
        listdiscountfactors = discount_factors(r, n, m)
    
        listpaymenttimes = cashflow_times(n,m)
        
        listpaymenttimesplus1 = [i + 2 for i in range (n*m)]
        
        pvcashflows = [a * b for a , b in zip(listcashflows,listdiscountfactors)]
        
        timefactor = [a * b for a , b in zip(listpaymenttimes,listpaymenttimesplus1)]
        
        numerator = [a *b for a , b in zip(pvcashflows,timefactor)]
        
        denominator = (bond_price(fv,c,n,m,r))*((1+r/m)**2)*m**2
        
        convexity = sum(numerator)/denominator
        
        return convexity
    
        
if __name__ ==  "__main__":
    
    #create a Bond object
    b1 = Bond(1000, 3, 0.05, 2)
    b2 = Bond(5000,5)
    b3 = Bond(5000,3,.05)
    b4 = Bond(1000,2,.06)
    #print(b1)
    #print(b1.set_price(950))
    #print(b1)