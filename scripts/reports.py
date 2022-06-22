# -*- coding: utf-8 -*-
"""
Модуль содержит функция для работы с текстовыми отчётами и сводными таблицами
"""
import os
import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append("d:/work")
import pandas as pd
import numpy as np
import func_db
from library import save_reports
from library import settings as stg
import graphics
os.chdir("d:/work/")


# Функция поиска машин выбранного дилера в ценовом диапазоне
# Текстовый отчёт 1
def cars_in_range(w: pd.DataFrame, dealer_name: str, low_lim: str, upper_lim: str) -> pd.DataFrame:
    """
    Показывает машины из заданного ценового диапазона в заданном магазине. 

    Parameters
    —------—
    w : pd.DataFrame
    dealer_name : str
    low_lim : str
    upper_lim : str

    Returns
    —---—
    pd.DataFrame

    Автор: Букина Валерия
    """

    sel1 = (w['Dealership'] == dealer_name) & (w['Price'] > low_lim) & (w['Price'] < upper_lim)
    sel2 = (w.columns != 'Gift') & (w.columns != 'Telephone')
    return w.loc[sel1, sel2]


# Функция, показывающая все имеющиеся машины опредленного бренда во всех салонах    
# Текстовый отчёт 2
def certain_car_brand(w: pd.DataFrame, brand_name: str) -> pd.DataFrame:
    """
    Показывает машины определенной фирмы и информацию о них.

    Parameters
    —------—
    w : pd.DataFrame
    brand_name : str

    Returns
    —---—
    pd.DataFrame

    Автор: Мартинич Андрей
    """
    sel = (w['Brand'] == brand_name)
    return w.loc[sel, :'Dealership']


# Показывает машины определенного дилера в порядке возрастания стоимости    
# Текстовый отчёт 3
def car_order_price(w: pd.DataFrame, dealer_name: str) -> pd.DataFrame:
    """
    Показывает машины в определенном магазине в порядке возрастания по цене.

    Parameters
    —------—
    w : pd.DataFrame
    dealer_name : str

    Returns
    -------
    pd.DataFrame

    Автор: Мартинич Андрей
    """
    sel = (w['Dealership'] == dealer_name)
    j = w.loc[sel, :'Dealership']
    return j.sort_values(by=['Price'])
    

# Сводная таблица, показывающая список подарков, которые выдаёт каждый салон 
# Сводная таблица 1
def dealership_gifts(w: pd.DataFrame, dealer_name: str) -> pd.DataFrame:
    """
    Показывает список подарков и машин, среднюю стоимость машин,
    предоставляемых определенным магазином.

    Parameters
    —------—
    w : pd.DataFrame
    dealer_name : str

    Returns
    —---—
    pd.DataFrame

    Автор: Грязева Ксения
    """
    sel = (w['Dealership'] == dealer_name)
    w = w.loc[sel, :]
    piv = pd.pivot_table(w, index=['Brand', 'Gift'], columns=['Dealership'],
                         values="Price", aggfunc='mean')
    for i in range(piv.shape[0]):
        piv.loc[piv.index[i][0],'Brand']=piv.index[i][0]
        piv.loc[piv.index[i][0],'Gift'] = piv.index[i][1]
        
    return piv


# Сводная таблица показывает общую стоимость машин опредленного бренда во всех салонах
# Сводная таблица 2
def car_common_price(w: pd.DataFrame) -> pd.DataFrame:
    """
    Показывает суммарную стоимость всех машин определенной фирмы.

    Parameters
    —------—
    w : pd.DataFrame

    Returns
    —---—
    pd.DataFrame

    Автор: Грязева Ксения

    """
    piv = pd.pivot_table(w, index=['Brand'], values="Price", aggfunc= np.sum)
    piv['Brand']=piv.index
    return piv


# Сводная таблица показывает, в каких салон есть данная марка машины
# Сводная таблица 3
def car_available(w: pd.DataFrame, brand_name: str) -> pd.DataFrame:
    """
    Показывает в каких магазинах находятся машины определенной фирмы.

    Parameters
    —------—
    w : pd.DataFrame
    brand_name : str

    Returns
    —---—
    pd.DataFrame

    Автор: Мартинич Андрей

    """
    sel = (w['Brand'] == brand_name)
    w = w.loc[sel, :]
    piv = pd.pivot_table(w, index=['Brand'], columns=['Dealership'],
                         values='Telephone', aggfunc='mean')
    piv['Brand']=piv.index
    return piv


def text_rep_1(new_window: tk.Toplevel, full_list: pd.DataFrame):
    """
    Функция создает новое окно и осуществляет реализацию текстового отчета 1

    Parameters
    ----------
    newWindow : tk.Toplevel
        виджет нового окна
    Full_list : pd.DataFrame
        база данных

    Returns
    -------
        -
    Автор: Букина Валерия

    """
    # Поля ввода для создания данного отчёта
    tk.Label(new_window, text='Данный отчет показывает машины из заданного ценового диапазона в заданном магазине.',
             bg=stg.fon, fg=stg.knop, font=7).place(x=55, y=320)

    d_name = tk.StringVar()
    tk.Label(new_window, text='Введите название автосалона:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=405)
    tk.Entry(new_window, textvariable=d_name).place(x=365, y=410)

    l_lim = tk.StringVar()
    tk.Label(new_window, text='Введите нижнюю ценовую границу:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=435)
    tk.Entry(new_window, textvariable=l_lim).place(x=365, y=440)

    u_lim = tk.StringVar()
    tk.Label(new_window, text='Введите верхнюю ценовую границу:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=465)
    tk.Entry(new_window, textvariable=u_lim).place(x=365, y=470)

    # Радиобатонны для выбора формата файла
    r1 = tk.IntVar()
    r2 = tk.IntVar()
    r3 = tk.IntVar()
    tk.Radiobutton(new_window, text='excel', value=1, variable=r1, bg=stg.knop).place(x=500, y=350)
    tk.Radiobutton(new_window, text='pickle', value=2, variable=r2, bg=stg.knop).place(x=500, y=380)
    tk.Radiobutton(new_window, text='csv', value=3, variable=r3, bg=stg.knop).place(x=500, y=410)

    def get_values1(new_window: tk.Toplevel):
        """
        Функция считывает значения полей Entry и Radiobutton
        и на их основе осущетствляет вывод и сохранение базы данных
        Parameters
        ----------
        new_window : tk.Toplevel
            виджет нового окна

        Returns
        -------
        -
        Автор: Букина Валерия
        """
        # Извлечение значений из полей Entry
        try:
            d_n_v = d_name.get()
            l_l_v = l_lim.get()
            u_l_v = u_lim.get()
            d = cars_in_range(full_list, d_n_v, int(l_l_v), int(u_l_v))
        except ValueError:
            messagebox.showwarning(message='Не корректно введены значения, повторите ввод')
        func_db.print_reports(d, new_window)

        rb1_v = r1.get()
        rb2_v = r2.get()
        rb3_v = r3.get()
        if (rb1_v == 0) & (rb2_v == 0) & (rb3_v == 0):
            messagebox.showwarning(message='Не выбран формат файла, выберите повторно!')
        # кнопка, сохраняющая отчёт
        tk.Button(new_window, text='Сохранить отчет',
                  bg=stg.knop,
                  activebackground='white',
                  font=7,
                  command=lambda: save_reports.choose_format_and_save(d, rb1_v, rb2_v, rb3_v)).place(x=690, y=410)

    # кнопка обработки значений из полей Entry и создания на их основе таблицы с необходимыми данными
    tk.Button(new_window,
              text='Создать отчет',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: get_values1(new_window)
              ).place(x=500, y=440)


def text_rep_2(new_window: tk.Toplevel, full_list: pd.DataFrame):
    """
    Функция создает новое окно и осуществляет реализацию текстового отчета 2

    Parameters
    ----------
    newWindow : tk.Toplevel
        виджет нового окна
    Full_list : pd.DataFrame
        база данных

    Returns
    -------
        -
        Автор: Букина Валерия
    """
    # Поля ввода для создания данного отчёта
    tk.Label(new_window, text='Данный отчет показывает машины определенной фирмы и информацию о них.',
             bg=stg.fon, fg=stg.knop, font=7).place(x=55, y=320)

    b_name = tk.StringVar()
    tk.Label(new_window, text='Введите марку автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=405)
    tk.Entry(new_window, textvariable=b_name).place(x=365, y=410)

    # Радиобатонны для выбора формата файла
    r1 = tk.IntVar()
    r2 = tk.IntVar()
    r3 = tk.IntVar()
    tk.Radiobutton(new_window, text='excel', value=1, variable=r1, bg=stg.knop).place(x=500, y=350)
    tk.Radiobutton(new_window, text='pickle', value=2, variable=r2, bg=stg.knop).place(x=500, y=380)
    tk.Radiobutton(new_window, text='csv', value=3, variable=r3, bg=stg.knop).place(x=500, y=410)

    def get_values2(newWindow: tk.Toplevel):
        """
        Функция считывает значения полей Entry и Radiobutton
        и на их основе осуществляет вывод и сохранение базы данных
        Parameters
        ----------
        new_window : tk.Toplevel
            виджет нового окна

        Returns
        -------
        -
        Автор: Букина Валерия
        """
        # Извлечение значений из полей Entry
        b_n_v = b_name.get()
        d = certain_car_brand(full_list, b_n_v)
        func_db.print_reports(d, new_window)

        rb1_v = r1.get()
        rb2_v = r2.get()
        rb3_v = r3.get()
        if (rb1_v == 0) & (rb2_v == 0) & (rb3_v == 0):
            messagebox.showwarning(message='Не выбран формат файла, выберите повторно!')
        # кнопка, сохраняющая отчёт
        tk.Button(newWindow, text='Сохранить отчет',
                  bg=stg.knop,
                  activebackground='white',
                  font=7,
                  command=lambda: save_reports.choose_format_and_save(d, rb1_v, rb2_v, rb3_v)).place(x=690, y=410)

    # кнопка обработки значений из полей Entry и создания на их основе таблицы с необходимыми данными
    tk.Button(new_window,
              text='Создать отчет',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: get_values2(new_window)
              ).place(x=500, y=440)


def text_rep_3(newWindow: tk.Toplevel, Full_list: pd.DataFrame):
    """
    Функция создает новое окно и осуществляет реализацию текстового отчета 3

    Parameters
    ----------
    newWindow : tk.Toplevel
        виджет нового окна
    Full_list : pd.DataFrame
        база данных

    Returns
    -------
        -
        Автор: Букина Валерия
    """
    # Поля ввода для создания данного отчёта

    tk.Label(newWindow, text='Данный отчет показывает машины в определенном магазине в порядке возрастания по цене.',
             bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=320)

    d_name = tk.StringVar()
    tk.Label(newWindow, text='Введите название автосалона:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=405)
    tk.Entry(newWindow, textvariable=d_name).place(x=365, y=410)

    # Радиобатонны для выбора формата файла
    r1 = tk.IntVar()
    r2 = tk.IntVar()
    r3 = tk.IntVar()
    tk.Radiobutton(newWindow, text='excel', value=1, variable=r1, bg=stg.knop).place(x=500, y=350)
    tk.Radiobutton(newWindow, text='pickle', value=2, variable=r2, bg=stg.knop).place(x=500, y=380)
    tk.Radiobutton(newWindow, text='csv', value=3, variable=r3, bg=stg.knop).place(x=500, y=410)

    def get_values3(newWindow: tk.Toplevel):
        """
        Функция считывает значения полей Entry и Radiobutton
        и на их основе осущетствляет вывод и сохранение базы данных
        Parameters
        ----------
        new_window : tk.Toplevel
            виджет нового окна

        Returns
        -------
        -
        Автор: Букина Валерия
        """
        # Извлечение значений из полей Entry
        d_n_v = d_name.get()
        D = car_order_price(Full_list, d_n_v)
        func_db.print_reports(D, newWindow)

        rb1_v = r1.get()
        rb2_v = r2.get()
        rb3_v = r3.get()
        if (rb1_v == 0) & (rb2_v == 0) & (rb3_v == 0):
            messagebox.showwarning(message='Не выбран формат файла, выберите повторно!')

        # кнопка, сохраняющая отчёт
        tk.Button(newWindow, text='Сохранить отчет',
                  bg=stg.knop,
                  activebackground='white',
                  font=7,
                  command=lambda: save_reports.choose_format_and_save(D, rb1_v, rb2_v, rb3_v)).place(x=690, y=410)

    # кнопка обработки значений из полей Entry и создания на их основе таблицы с необходимыми данными
    tk.Button(newWindow,
              text='Создать отчет',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: get_values3(newWindow)
              ).place(x=500, y=440)


def piv_rep_1(newWindow: tk.Toplevel, Full_list: pd.DataFrame):
    """
    Создает интерфейс для создания 1 сводной таблицы

    Parameters
    ----------
    newWindow : tk.Toplevel
        виджет нового окна
    Full_list : pd.DataFrame
        база данных 

    Returns
    -------
        -
        Автор: Грязева Ксения

    """
    # Поля ввода для создания данного отчёта
    tk.Label(newWindow,
             text='Данная сводная таблица показывает список подарков, машин, общую стоимость машин,' + '\n' + ' предоставляемых определенным магазином.',
             bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=320)

    d_name = tk.StringVar()
    tk.Label(newWindow, text='Введите название автосалона:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=405)
    tk.Entry(newWindow, textvariable=d_name).place(x=365, y=410)

    # Радиобатонны для выбора формата файла
    r1 = tk.IntVar()
    r2 = tk.IntVar()
    r3 = tk.IntVar()
    tk.Radiobutton(newWindow, text='excel', value=1, variable=r1, bg=stg.knop).place(x=480, y=380)
    tk.Radiobutton(newWindow, text='pickle', value=2, variable=r2, bg=stg.knop).place(x=550, y=380)
    tk.Radiobutton(newWindow, text='csv', value=3, variable=r3, bg=stg.knop).place(x=550, y=410)

    def get_values_piv1(newWindow: tk.Toplevel):
        """
        Функция считывает значения полей Entry и Radiobutton
        и на их основе осуществляет вывод и сохранение базы данных
        Parameters
        ----------
        new_window : tk.Toplevel
            виджет нового окна

        Returns
        -------
        -
        Автор: Грязева Ксения
        """
        # Извлечение значений из полей Entry и Radiobutton
        d_n_v = d_name.get()
        D = dealership_gifts(Full_list, d_n_v)
        func_db.print_piv_table(D, newWindow)

        rb1_v = r1.get()
        rb2_v = r2.get()
        rb3_v = r3.get()
        if (rb1_v == 0) & (rb2_v == 0) & (rb3_v == 0):
            messagebox.showwarning(message='Не выбран формат файла, выберите повторно!')

        # кнопка, сохраняющая отчёт
        tk.Button(newWindow, text='Сохранить отчет',
                  bg=stg.knop,
                  activebackground='white',
                  font=7,
                  command=lambda: save_reports.choose_format_and_save(D, rb1_v, rb2_v, rb3_v)).place(x=690, y=410)

    # кнопка обработки значений из полей Entry и создания на их основе таблицы с необходимыми данными
    tk.Button(newWindow,
              text='Создать отчет',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: get_values_piv1(newWindow)
              ).place(x=500, y=440)


def piv_rep_2(newWindow: tk.Toplevel, Full_list: pd.DataFrame):
    """
    Создает интерфейс для создания 2 сводной таблицы

    Parameters
    ----------
    newWindow : tk.Toplevel
        виджет нового окна
    Full_list : pd.DataFrame
        база данных 

    Returns
    -------
        -
        Автор: Грязева Ксения

    """
    tk.Label(newWindow, text='Данная сводная таблица показывает суммарную стоимость всех машин определенной фирмы.',
             bg=stg.fon, fg=stg.knop, font=7).place(x=15, y=320)
    # Радиобатонны для выбора формата файла
    r1 = tk.IntVar()
    r2 = tk.IntVar()
    r3 = tk.IntVar()
    tk.Radiobutton(newWindow, text='excel', value=1, variable=r1, bg=stg.knop).place(x=500, y=350)
    tk.Radiobutton(newWindow, text='pickle', value=2, variable=r2, bg=stg.knop).place(x=500, y=380)
    tk.Radiobutton(newWindow, text='csv', value=3, variable=r3, bg=stg.knop).place(x=500, y=410)

    def get_values_piv2(newWindow: tk.Toplevel):
        """
        Функция считывает значения полей Entry и Radiobutton
        и на их основе осущетствляет вывод и сохранение базы данных
        Parameters
        ----------
        new_window : tk.Toplevel
            виджет нового окна

        Returns
        -------
        -
        Автор: Грязева Ксения
        """
        # Извлечение значений из полей Entry и Radiobutton
        D = car_common_price(Full_list)
        func_db.print_piv_table(D, newWindow)

        rb1_v = r1.get()
        rb2_v = r2.get()
        rb3_v = r3.get()

        if (rb1_v == 0) & (rb2_v == 0) & (rb3_v == 0):
            messagebox.showwarning(message='Не выбран формат файла, выберите повторно!')

        # кнопка, сохраняющая отчёт
        tk.Button(newWindow, text='Сохранить отчет',
                  bg=stg.knop,
                  activebackground='white',
                  font=7,
                  command=lambda: save_reports.choose_format_and_save(D, rb1_v, rb2_v, rb3_v)).place(x=690, y=410)

    # кнопка обработки значений из полей Entry и создания на их основе таблицы с необходимыми данными
    tk.Button(newWindow, text='Создать отчет',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: get_values_piv2(newWindow)
              ).place(x=500, y=440)


def piv_rep_3(newWindow: tk.Toplevel, Full_list: pd.DataFrame):
    """
    Создает интерфейс для создания 3 сводной таблицы

    Parameters
    ----------
    newWindow : tk.Toplevel
        виджет нового окна
    Full_list : pd.DataFrame
        база данных 

    Returns
    -------
        -
        Автор: Грязева Ксения

    """
    
    # Поля ввода для создания данного отчёта
    tk.Label(newWindow,
             text='Данная сводная таблица показывает в каких магазинах находятся машины определенной\n фирмы и номер телефона этих салонов.',
             bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=320)

    b_name = tk.StringVar()
    tk.Label(newWindow, text='Введите марку автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=405)
    tk.Entry(newWindow, textvariable=b_name).place(x=365, y=410)

    # Радиобатонны для выбора формата файла
    r1 = tk.IntVar()
    r2 = tk.IntVar()
    r3 = tk.IntVar()
    tk.Radiobutton(newWindow, text='excel', value=1, variable=r1, bg=stg.knop).place(x=440, y=380)
    tk.Radiobutton(newWindow, text='pickle', value=2, variable=r2, bg=stg.knop).place(x=500, y=380)
    tk.Radiobutton(newWindow, text='csv', value=3, variable=r3, bg=stg.knop).place(x=500, y=410)

    def get_values_piv3(newWindow: tk.Toplevel):
        """
        Функция считывает значения полей Entry и Radiobutton
        и на их основе осуществляет вывод и сохранение базы данных
        Parameters
        ----------
        new_window : tk.Toplevel
            виджет нового окна

        Returns
        -------
        -
        Автор: Грязева Ксения
        """
        # Извлечение значений из полей Entry и Radiobutton
        b_n_v = b_name.get()
        D = car_available(Full_list, b_n_v)
        func_db.print_piv_table(D, newWindow)

        rb1_v = r1.get()
        rb2_v = r2.get()
        rb3_v = r3.get()
        if (rb1_v == 0) & (rb2_v == 0) & (rb3_v == 0):
            messagebox.showwarning(message='Не выбран формат файла, выберите повторно!')

        # кнопка, сохраняющая отчёт
        tk.Button(newWindow, text='Сохранить отчет',
                  bg=stg.knop,
                  activebackground='white',
                  font=7,
                  command=lambda: save_reports.choose_format_and_save(D, rb1_v, rb2_v, rb3_v)).place(x=690, y=410)

    # кнопка обработки значений из полей Entry и создания на их основе таблицы с необходимыми данными
    tk.Button(newWindow, text='Создать отчет',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: get_values_piv3(newWindow)
              ).place(x=500, y=440)


def graph_report_scatter(w:pd.DataFrame):
    """
    Функция создает графический отчет: какой сувенир у какой фирмы

    Parameters
    ----------
    w : pd.DataFrame
        база данных

    Returns
    -------
    -
    Автор: Мартинич Андрей
    """
    try: 
        graphics.scatter(w['Brand'], w['Gift'])
    except TypeError:
        messagebox.showwarning(message='Для одной из марок данные некорректны. Повторите ввод сувениров')


def graph_report_bar(w:pd.DataFrame):
    """
    Функция создает графический отчет: суммарная стоимость каждой марки

    Parameters
    ----------
    w : pd.DataFrame
        база данных

    Returns
    -------
    -
    Автор: Мартинич Андрей
    """
    try: 
        d = car_common_price(w)
        graphics.average_bar(d)
    except TypeError:
        messagebox.showwarning(message='Для одной из марок данные некорректны. Проверьте данные')    
    
def graph_report_hist(w: pd.DataFrame):
    """
    Функция создает графический отчет: количество машин в каждом автосалоне

    Parameters
    ----------
    w : pd.DataFrame
        база данных

    Returns
    -------
    -
    Автор: Грязева Ксения
    """
    try: 
        graphics.dealer_hist(w)
    except TypeError:
        messagebox.showwarning(message='Для одной из марок данные некорректны. Проверьте данные') 
 
    
def graph_report_box(newWindow: tk.Toplevel, w: pd.DataFrame):
    """
    Функция создает графический отчет: отношение стоимости машин в определенном салоне

    Parameters
    ----------
    w : pd.DataFrame
        база данных
    newWindow: tk.Toplevel
    Returns
    -------
    -
    Автор: Грязева Ксения
    """
    
    d_name = tk.StringVar()
    tk.Label(newWindow, text='Введите название автосалона:', bg=stg.fon, fg=stg.knop, font=7).place(x=25, y=100)
    tk.Entry(newWindow, textvariable=d_name).place(x=105, y=140)
    
    
    def make_graph(w: pd.DataFrame):
        """
        Функция, осуществляющая создание диаграммы

        Parameters
        ----------
        w : pd.DataFrame
            база данных

        Returns
        -------
            -
        Автор: Грязева Ксения
        """
        dname = d_name.get() 
        try: 
            graphics.boxplot(w, dname)
        except TypeError:
            messagebox.showwarning(message='Для одной из марок данные некорректны. Проверьте данные')
            
    tk.Button(newWindow, text='Создать график',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: make_graph(w)).place(x=105, y=250) 
    
    
def table_by_path(path: str) -> pd.DataFrame:
    """
    Возвращает  таблицу с данными по заданному пути

    Parameters
    ----------
    path : str
        путь

    Returns
    -------
    table : pd.DataFrame
        база данных

       Автор: Мартинич Андрей
    """
    table = pd.read_pickle(path)
    return table
