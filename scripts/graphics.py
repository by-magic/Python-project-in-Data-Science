# -*- coding: utf-8 -*-
"""
Модуль с функциями для графических отчётов
"""
import matplotlib.pyplot as plt
import pandas as pd
                                                                             
def scatter(atr1: pd.Series, atr2: pd.Series):
    """
    Функция, создающая график, показывающий у какой марки какой сувенир

    Parameters
    ----------
    atr1 : pd.Series
        список марок
    atr2 : pd.Series
        список сувениров

    Returns
    -------
        -
        Автор: Мартинич Андрей
    """
    fig = plt.figure(figsize=(18,5))
    ax = fig.add_subplot()
    x = atr1
    y = atr2
    ax.scatter(x,y)
    ax.grid()
    plt.show()
   
def average_bar(w: pd.DataFrame):
    """
    Функция, создающая график, показывающий суммарную стоимость каждой марки

    Parameters
    ----------
    w : pd.DataFrame
        база данных

    Returns
    -------
        -
        Автор: Мартинич Андрей
    """
    fig = plt.figure(figsize=(18,5))
    ax = fig.add_subplot()
    x = w['Brand']
    y = w['Price']
    ax.bar(x,y)
    ax.grid()
    plt.show()

def dealer_hist(w: pd.DataFrame):
    """
    Функция, создающая график гистограмму, который показывает количество машин в каждом из автосалонов

    Parameters
    ----------
    w : pd.DataFrame
       база данных

    Returns
    -------
    -
    Автор: Букина Валерия
    """
    plt.ylabel(r'Количество различных машин', fontsize=16)
    plt.hist(w['Dealership'])
    plt.show()

def boxplot(w: pd.DataFrame, dealer_name: str):
    """
    Функция, создающая график Бокса-Вискера, который показывает отношения стоимости 
    машин в определенном салоне
    
    Parameters
    ----------
    w : pd.DataFrame
        база данных
    dealer_name: str
        название автосалона
    
    Returns
    -------
    -
        Автор: Грязева Ксения
    """
    fig = plt.figure(figsize=(9,9))
    ax = fig.add_subplot()
    ax.set_title(dealer_name)
    sel1 = w['Dealership'] == dealer_name
    ta = w[sel1]
    plt.boxplot(ta['Price'])   
    plt.show()   