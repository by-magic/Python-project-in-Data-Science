# -*- coding: utf-8 -*-
"""
    Модуль с функциями сохранения отчетов в различные форматы
"""
import pandas as pd
from tkinter import filedialog as fd


def save_text_report_excel(w: pd.DataFrame):
    """
    Сохраняет базу данных (сформированный текстовый отчет) в формате Excel по пути,
    который выбрал пользователь

    Parameters
    ----------
    w : pd.DataFrame
        база данных сформированного отчета

    Returns
    -------
        -
    Автор:Грязева Ксения

    """

    name = fd.asksaveasfilename(defaultextension='.xlsx')
    if name:
        w.to_excel(name, index=False)


def save_text_report_pickle(w: pd.DataFrame):
    """
    Сохраняет базу данных (сформированный текстовый отчет) в формате pickle по пути,
    который выбрал пользователь

    Parameters
    ----------
    w : pd.DataFrame
        база данных сформированного отчета

    Returns
    -------
        -
    Автор: Букина Валерия

    """

    name = fd.asksaveasfilename(defaultextension='.pkl')
    if name:
        w.to_pickle(name)


def save_text_report_csv(w: pd.DataFrame):
    """
    Сохраняет базу данных (сформированный текстовый отчет) в формате csv по пути,
    который выбрал пользователь

    Parameters
    ----------
    w : pd.DataFrame
        база данных сформированного отчета

    Returns
    -------
        -
    Автор: Букина Валерия

    """

    name = fd.asksaveasfilename(defaultextension='.csv')
    if name:
        w.to_csv(name, index=False, sep=";")


def choose_format_and_save(w: pd.DataFrame, r1: int, r2: int, r3: int):
    """
    Анализирует с помощью значений Radiobutton r1,r2,r3 выбранные форматы файла
    и сохраняет базу данных (текстовый отчет) в данном формате

    Parameters
    ----------
    w : pd.DataFrame
        база данных сформированного отчета
    r1 : int
        значение Radiobutton excel
    r2 : int
        значение Radiobutton pickle
    r3 : int
        значение Radiobutton csv

    Returns
    -------
        -
    Автор: Мартинич Андрей
    """
    if (r1 == 1):
        save_text_report_excel(w)
    if (r2 == 2):
        save_text_report_pickle(w)
    if (r3 == 3):
        save_text_report_csv(w)
