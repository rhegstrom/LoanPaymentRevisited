# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:11:35 2022

@author: rhegstrom
"""

import numpy as np
import math

class loanpy(object):
    def __init__ (self, name):  # initialize with a name, thie permits
                                # easier manamgement of multiple instances
        """
        loanpy is a class object to implement computations of 
        loan parameters
        
        name documents data set

        Returns
        -------
        None.

        """
        #initialization
        self._name = name
        self._Pv = 0
        self._rateAPR = 0
        self._Pmt = 0
        self._nMonths=0
        
        
    def getName(self):
        print(f"\nname on this instance: {self._name}")
    
    def getChoice(self):
        print("\nwhat would you like to compute?")
        print("options: Pmt, Pv, rateAPR, nMonths")
        
        choice = 0
        
        while choice  not in ("Pmt", "Pv", "rateAPR", "nMonths"):
            choice = input("enter choice ")
            
        if choice == "Pmt":
            self.getPmt()
        elif choice == 'Pv':
            self.getPv()
        elif choice == 'rateAPR':
            self.getIntRate()
        else:
            self.get_nMonths()


    def getIntRate(self):
        ''' Solve for interest rate, APR  '''
        self._Pv = float(input('Enter PV '))
        self._Pmt = float(input('Enter Pmt '))
        self._nMonths = int(input('Enter number of months '))
        
        # The solution will be r where using Pmt, n, and Pv works
        ## bisection algorithm finds the two sides of the equation are equal
        ## that is, the difference is 0
        ## side 1: Pmt*(1-(1+r)**(-n))
        ## side 2:  Pv*r
        
        #example of an in-line (lambda) function
        fIntRate = lambda r: self._Pmt*(1-(1+r)**(-self._nMonths)) - self._Pv*r
        
        # low and high possible interest rates, APR
        # the actual rate is between 
        
        _rlow =0
        _rhigh = 50 
        
        _rl = _rlow/1200
        _rh = _rhigh/1200
        _count = 0
        
        while(_count < 20): # in case there is no solution
            _rTry = (_rl+_rh)/2
            if abs(fIntRate(_rTry)) < 0.001: break
            
            if fIntRate(_rTry) > 0: _rl = _rTry
            else: _rh = _rTry
            
            _count += 1
            
        if(_count >=20):
            print("no solution: try again")
            print(f"interest rate APR is > {_rTry*1200:.2f}%") # convert back to APR
            rTry = None
        
        print(f"Interest rate is {_rTry*1200:.2f}%")
    

    def getPmt(self):
        self._Pv = float(input("Enter Loan Amount: "))        
        self._rateAPR = float(input("Enter APR: "))
        self._nMonths = int(input("Enter Months: "))

        self._Pmt = self._rateAPR / 1200 * self._Pv / (1 - (1 + (self._rateAPR / 1200 )) ** (-self._nMonths))
        print(f"Your monthly payments will be ${self._Pmt:,.2f}")
        pass
    
    
    
    def get_nMonths(self):
        # formula: nMonths = -np.log(1 - (self._Pv * _r / self._Pmt)) / np.log(1 + _r)
        self._rateAPR = float(input("Enter APR: "))
        self._Pv = int(input("Enter Loan Amount: "))
        self._Pmt = float(input("Enter Monthly Pmt: "))
        
        _r = self._rateAPR / 1200
        
        self._nMonths = -np.log(1 - (self._Pv * _r / self._Pmt)) / np.log(1 + _r)
        print(f"It will take you {math.ceil(self._nMonths)} months to pay off that loan.")
        pass
    
    
    def getPv(self):
        self._rateAPR = float(input("Enter APR: "))
        self._nMonths = int(input("Enter Months: "))
        self._Pmt = float(input("Enter Pmt: "))
        
        Amt = (self._Pmt * 1200 * (-(self._rateAPR/1200+1)**-self._nMonths + 1 )) / self._rateAPR
        print(f"Loan amount is ${Amt:,.2f}")
        pass


#####################################################################     
  
if __name__ == '__main__':
    
    testloan = loanpy('car')
    testloan.getName()
    
    testloan.getChoice()



"""
APR = 10.0   # apr
Term = 48     # term

print(f'APR={APR}, Term={Term}')

Pmt = int(input('Payment amount -->'))
Amt = (Pmt * 1200 * (-(APR/1200+1)**-Term + 1 )) / APR

print(f"loan amt={Amt}")
"""