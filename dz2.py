# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:30:31 2022

@author: Ksenia
"""
import pandas as pd
import numpy as np
import os
os.chdir("d:/work/")

Full_list=pd.read_excel("C:/Users/Ksenia/Desktop/python в науке о данных/nf1.xlsx")
Dealership=pd.read_excel("C:/Users/Ksenia/Desktop/python в науке о данных/tb1.xlsx")
Gift=pd.read_excel("C:/Users/Ksenia/Desktop/python в науке о данных/tb3.xlsx")
Phones=pd.read_excel("C:/Users/Ksenia/Desktop/python в науке о данных/tb2.xlsx")

def cars_in_range(W: pd.DataFrame, dealer_name: str, low_lim: str, upper_lim: str)->pd.DataFrame:
    """
    Shows cars in a given price range at a given dealership
    
    Parameters
    —------—
    W : pd.DataFrame
    dealer_name : str
    low_lim : str
    upper_lim : str
    
    Returns
    —---—
    pd.DataFrame
    
    """
    sel1 = (W['Dealership'] == dealer_name) & (W['Price']>low_lim) & (W['Price']<upper_lim)
    sel2 = (W.columns != 'Gift')& (W.columns != 'Telephone')
    return W.loc[sel1,sel2]
    
    
Q = cars_in_range(Full_list, 'Top auto', 4000000, 15000000)
    
def certain_car_brand(W: pd.DataFrame, brand_name: str)->pd.DataFrame:
    """
    Shows all cars of a certain brand and information about them
    
    Parameters
    —------—
    W : pd.DataFrame
    brand_name : str
    
    Returns
    —---—
    pd.DataFrame
    
    """
    sel = (W['Brand'] == brand_name)  
    return W.loc[sel, :]
    
    
E = certain_car_brand(Full_list,'Audi')
    
def car_order_price(W: pd.DataFrame, dealer_name: str)->pd.DataFrame:
    
    """
    Shows all cars in this car dealership in ascending order of price
    
    Parameters
    —------—
    W : pd.DataFrame
    dealer_name : str

    Returns
    -------
    pd.DataFrame

    """
    #int mi = 100000000000
    sel = (W['Dealership'] == dealer_name)  
    for i in W['Price'].length:
        if i < mi:
            W[['Index']]
    return W.loc[sel, :]
    
    
R = certain_car_brand(Full_list,'Real auto')
    
#svodnye tablitsi       
      
def dealership_gifts(W: pd.DataFrame, dealer_name: str)->pd.DataFrame:
    """
    Shows a list of gifts that a certain car dealership gives out
    
    Parameters
    —------—
    W : pd.DataFrame
    dealer_name : str
    
    Returns
    —---—
    pd.DataFrame
    
    """ 
    sel = (W['Dealership']==dealer_name)
    W = W.loc[sel, :]
    piv = pd.pivot_table(W, index = ['Dealership','Gift'], columns = ['Brand'],
                                    values = "Price", aggfunc = 'mean')
    return piv

T = dealership_gifts(Full_list, 'Real auto')
    
def car_common_price(W: pd.DataFrame)->pd.DataFrame:
    """
    Shows the total cost of all models of a certain car brand
    
    Parameters
    —------—
    W : pd.DataFrame
    
    Returns
    —---—
    pd.DataFrame
    
    """ 
 
    piv = pd.pivot_table(W, index = ['Brand'], values = "Price", aggfunc = 'mean')
    return piv

Y = car_common_price(Full_list)

def car_available(W: pd.DataFrame, brand_name: str)->pd.DataFrame:
    """
    Shows in which stores this car brand is available
    
    Parameters
    —------—
    W : pd.DataFrame
    brand_name : str
    
    Returns
    —---—
    pd.DataFrame
    
    """ 
    sel = (W['Brand']==brand_name)
    W = W.loc[sel, :]
    piv = pd.pivot_table(W, index = ['Brand'], columns = ['Dealership'],
                                    values = "Telephone", aggfunc = 'mean')
    return piv

U = car_available(Full_list, 'BMW')
