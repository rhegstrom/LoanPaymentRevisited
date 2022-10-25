# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:11:35 2022

@author: Roger Hegstrom(rhegstrom@avc.edu)

We want to construct a class called 'loan'

in this class I want 4 functions:

1  given PV, nMonths, intAPR, compute the monthly payment   name this function computePmt(PV, intAPR, nMonths)
2  given PV, nMonths and monthly payment, Pmt, compute intAPR  name this function compute_intAPR(PV, nMonths, Pmt)
3. given PV, Pmt, intAPR compute the number of months, nMonths name this function compute_nMonths(PV, Pmt, intAPR)
4. given Pmt, intApr, nMonths compute PV, name this function computePV(Pmt, intAPR, nMonths)

For example if I wanted to compute Pmt I would use loan.computePmt(PV, intAPR, nMonths)

"""

import numpy as np
import math

class loanpy(object):
    def __init__ (self): 
        return None
       
    def compute_Pmt(self, amt, apr, term):
        """
        Returns the monthly payment of the loan

        Parameters
        ----------
        amt : float
            Loan amount in dollars.
        apr : float
            Loan interest rate percentage.
        term : int
            Loan term in months.

        Returns
        -------
        float
            Payment amount in dollars.

        """
        return np.round(apr / 1200 * amt / (1 - (1 + (apr / 1200 )) ** (-term)), 2)
    
    def compute_nMonths(self, amt, pmt, apr):
        """
        Returns the calculated loan term

        Parameters
        ----------
        amt : float
            Loan amount in dollars.
        pmt : float
            Payment amount in dollars.
        apr : float
            Loan interest rate percentage.

        Returns
        -------
        int
            Loan term in months.

        """
        return math.ceil(-np.log(1 - (amt * (apr / 1200) / pmt)) / np.log(1 + (apr / 1200)))
    
    def compute_PV(self, pmt, apr, term):
        """
        Returns the computed loan amount

        Parameters
        ----------
        pmt : float
            Payment amount in dollars.
        apr : float
            Loan interest rate percentage.
        term : int
            Loan term in months.

        Returns
        -------
        float
            Loan amount in dollars.

        """
        return math.floor((pmt * 1200 * (-(apr/1200+1)**-term + 1 )) / apr)

    def compute_intAPR(self, amt, pmt, term):       
        """
        Returns the computed loan interest rate

        Parameters
        ----------
        amt : float
            Loan amount in dollars.
        pmt : float
            Payment amount in dollars.
        term : int
            Loan term in months.

        Returns
        -------
        float
            Loan interest rate percentage.

        """
        # The solution will be r where using Pmt, n, and Pv works
        ## bisection algorithm finds the two sides of the equation are equal
        ## that is, the difference is 0
        ## side 1: Pmt*(1-(1+r)**(-n))
        ## side 2:  Pv*r
        
        #example of an in-line (lambda) function
        fIntRate = lambda r: pmt*(1-(1+r)**(-term)) - amt*r
        
        # low and high possible interest rates, APR
        # the actual rate is between 
        
        _rlow, _rhigh = 0, 50
        _rl, _rh      = _rlow/1200, _rhigh/1200
        _count        = 0
        
        while(_count < 20): # in case there is no solution
            _rTry = (_rl+_rh)/2
            if abs(fIntRate(_rTry)) < 0.001: break
            
            if fIntRate(_rTry) > 0: _rl = _rTry
            else: _rh = _rTry
            
            _count += 1
            
        if(_count >= 20):
            return None
        
        return np.round(_rTry*1200, 2)

              

def getValues(inputs):
    ret_vals = {}
    for inp in inputs:
        if inp == 'amt':
            ret_vals['amt']  = float(input('Enter loan amount: '))
        elif inp == 'pmt':
            ret_vals['pmt']  = float(input('Enter payment amount: '))
        elif inp == 'apr':
            ret_vals['apr']  = float(input('Enter interest rate(%): '))
        elif inp == 'term':
            ret_vals['term'] = int(input('Enter loan term: '))
            
    return ret_vals

#######################################################################################################
# Main loop creates object lp of class loanpy and uses the class's functions to calculate loan variables
########################################################################################################
# lp.compute_Pmt(amt, apr, term)
# lp.compute_PV(pmt, apr, term)
# lp.compute_nMonths(amt, pmt, apr)
# lp.compute_intAPR(amt, pmt, term)

if __name__ == '__main__':
    lp = loanpy()
    while True:
        print("\n\nPlease pick an loan item to calculate(Pmt, PV, intAPR, nMonths)")
        ch = input('choice> ')
        
        if ch == 'Pmt':
            vals = getValues(['amt', 'apr', 'term'])            
            pmt = lp.compute_Pmt(amt = vals['amt'], apr = vals['apr'], term = vals['term'])
            print(f'The calculated payment is ${pmt:.2f}/month.')
            
        elif ch == 'PV':
            vals = getValues(['pmt','apr','term'])
            pv = lp.compute_PV(pmt = vals['pmt'], apr = vals['apr'], term = vals['term'])
            print(f'The calculated loan amount is: ${pv:.2f}.')

        elif ch == 'nMonths':
            vals = getValues(['amt', 'pmt', 'apr'])
            term = lp.compute_nMonths(amt = vals['amt'], pmt = vals['pmt'], apr = vals['apr'])
            print(f'The calculated number of months is {term} months.')        
            
        elif ch == 'intAPR':
            vals = getValues(['amt', 'pmt', 'term'])
            apr = lp.compute_intAPR(amt = vals['amt'], pmt = vals['pmt'], term = vals['term'])
            if apr == None:
                print('error: could not calculate interest rate..')
            else:
                print(f'The calculated interest rate is {apr:.2f}%.')
        
