# -*- coding: utf-8 -*-
"""
Модуль с функциями для работы с базой данных
"""
import tkinter as tk
from tkinter import ttk
import os
import sys
sys.path.append("d:/work")
import pandas as pd
import reports
from library import settings as stg
os.chdir("d:/work/")


# Функция, создаяющая общую таблицу из 3 составляющих
def make_table(df1: pd.DataFrame, df2: pd.DataFrame, df3: pd.DataFrame) -> pd.DataFrame:
    """
    Функция осуществляет создание таблицы, отображающей всю информацию из всех таблиц

    Parameters
    ----------
    df1 : pd.DataFrame
        таблица с моделями машин
    df2 : pd.DataFrame
        таблица с телефонами автосалона
    df3 : pd.DataFrame
        таблица с сувенирами каждого бренда

    Returns
    -------
    df4 : pd.DataFrame
        полная таблица

    Автор: Мартинич Андрей 
    """
    df4 = pd.merge(df3, pd.merge(df1, df2, on=['Dealership']), on='Brand')
   
    return df4


# Функция вывода баз данных на главный экран
def print_all(w: pd.DataFrame, root: tk.Tk):
    """
    Функция выводит на экран текущую базу данных
    Parameters
    ----------
    w : pd.DataFrame
        база данных

    root : tk.Tk
        виджет, создающий новое окно

    Returns
    -------
        -
    Автор: Грязева Ксения

    """

    canvas_new = tk.Canvas(root, width=1000, height=500, bg=stg.fon)
    canvas_new.place(x=10, y=250)

    db_frame = tk.Frame(canvas_new, bg=stg.fon,
                        width=800,
                        height=900)
    db_frame.place(x=0, y=0)

    table = ttk.Treeview(db_frame)
    table['columns'] = list(w.columns)
    for column in table['columns']:
        table.heading(column, text=column)
        table.column(column, width=120, anchor=tk.CENTER)
    i = iter(w.index)
    for value in w.values:
        table.insert('', 'end', next(i), values=list(value))
    table.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2)

    # Скроллбар
    vscrollbar = tk.Scrollbar(db_frame, orient='vert', command=table.yview)
    table['yscrollcommand'] = vscrollbar.set
    vscrollbar.grid(row=0, column=1, sticky='nse')
    db_frame.rowconfigure(0, weight=1)
    db_frame.columnconfigure(0, weight=1)


# Функция вывода отчётов
def print_reports(w: pd.DataFrame, root: tk.Tk):
    """
    Функция выводит на экран текущий текстовый отчёт
    Parameters
    ----------
    w : pd.DataFrame
        база данных

    root : tk.Tk
        виджет, создающий новое окно

    Returns
    -------
        -
    Автор: Букина Валерия

    """

    canvas_new = tk.Canvas(root, width=890, height=300, bg=stg.fon)
    canvas_new.place(x=10, y=10)

    db_frame = tk.Frame(canvas_new, bg=stg.fon,
                        width=800,
                        height=900)
    db_frame.place(x=0, y=0)

    table = ttk.Treeview(db_frame)
    table['columns'] = list(w.columns)
    for column in table['columns']:
        table.heading(column, text=column)
        table.column(column, width=120, anchor=tk.CENTER)
    i = iter(w.index)
    for value in w.values:
        table.insert('', 'end', next(i), values=list(value))
    table.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2)
    # Скроллбар
    vscrollbar = tk.Scrollbar(db_frame, orient='vert', command=table.yview)
    table['yscrollcommand'] = vscrollbar.set
    vscrollbar.grid(row=0, column=1, sticky='nse')
    db_frame.rowconfigure(0, weight=1)
    db_frame.columnconfigure(0, weight=1)

                                            
# Функция вывода сводных таблиц
def print_piv_table(w: pd.DataFrame, root: tk.Tk):
    """
    Функция выводит на экран текущую сводную таблицу
    Parameters
    ----------
    w : pd.DataFrame
        база данных

    root : tk.Tk
        виджет, создающий новое окно

    Returns
    -------
        -
    Автор: Букина Валерия

    """

    canvas_new = tk.Canvas(root, width=890, height=300, bg=stg.fon)
    canvas_new.place(x=10, y=10)

    db_frame = tk.Frame(canvas_new, bg=stg.fon,
                        width=800,
                        height=900)
    db_frame.place(x=0, y=0)

    table = ttk.Treeview(db_frame)
    table['columns'] = list(w.columns)
    for column in table['columns']:
        table.heading(column, text=column)
        table.column(column, width=150, anchor=tk.CENTER)
    i = iter(w.index)
    for value in w.values:
        table.insert('', 'end', next(i), values=list(value))
    table.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2)
    # Скроллбар
    vscrollbar = tk.Scrollbar(db_frame, orient='vert', command=table.yview)
    table['yscrollcommand'] = vscrollbar.set
    vscrollbar.grid(row=0, column=1, sticky='nse')
    db_frame.rowconfigure(0, weight=1)
    db_frame.columnconfigure(0, weight=1)


# Функция удаления строки из базы данных
def delete_item(newWindow: tk.Tk, tb1: pd.DataFrame, tb2: pd.DataFrame, tb3: pd.DataFrame):
    """
    Функция, осуществляющая удаления текущей записи из базы данных
    Parameters
    ----------
    newWindow : tk.Tk
        виджет, создающий новое окно.
    tb1 : pd.DataFrame
        таблица с моделями машин 
    tb2 : pd.DataFrame
        таблица с телефонами каждого автосалона
    tb3 : pd.DataFrame
        таблица с сувенирами каджой марки машины
    Returns
    -------
        -
    Автор: Мартинич Андрей

    """

    # Текстовое пояснение полей для удаления
    c_name = tk.StringVar()
    tk.Label(newWindow, text='Введите номер изменяемой таблицы:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=5)
    tk.Entry(newWindow, textvariable=c_name).place(x=365, y=10)

    tk.Label(newWindow, text='Для изменения 1 таблицы - Модели:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=50)
    m_name = tk.StringVar()
    tk.Label(newWindow, text='Введите модель автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=30, y=95)
    tk.Entry(newWindow, textvariable=m_name).place(x=365, y=100)

    tk.Label(newWindow, text='Для изменения 2 таблицы - Телефоны:', bg=stg.fon, fg=stg.knop, font=7).place(x=10,
                                                                                                              y=140)

    d_name = tk.StringVar()
    tk.Label(newWindow, text='Введите название автосалона:', bg=stg.fon, fg=stg.knop, font=7).place(x=30, y=180)
    tk.Entry(newWindow, textvariable=d_name).place(x=365, y=185)

    tk.Label(newWindow, text='Для изменения 3 таблицы - Сувениры:', bg=stg.fon, fg=stg.knop, font=7).place(x=10,
                                                                                                              y=220)

    b_name = tk.StringVar()
    tk.Label(newWindow, text='Введите марку автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=30, y=250)
    tk.Entry(newWindow, textvariable=b_name).place(x=365, y=255)

    # Функция удаления и сохранения значений
    def save_values_del(tb1: pd.DataFrame, tb2: pd.DataFrame, tb3: pd.DataFrame):
        """
        Функция производит удаление определенной информации из указанной пользователем таблицы
        Если данное изменение таблицы ведёт к изменению других таблиц, то соответсвующие значения будут удалены
        ----------
        tb1 : pd.DataFrame
            таблица с моделями машин 
        tb2 : pd.DataFrame
            таблица с телефонами каждого автосалона
        tb3 : pd.DataFrame
            таблица с сувенирами каджой марки машины

        Returns
        -------
            -
        Автор: Мартинич Андрей

        """
        count = c_name.get()
        dc = {}
        dc['Brand'] = b_name.get()
        dc['Model'] = m_name.get()
        dc['Dealership'] = d_name.get()

        # Из 1 таблицы можно удалять только определенные модели машин
        # Именно модели, так как они однозначно определяют и марку, и цену и тд.
        if (int(count) == 1):
            idx = tb1.index[tb1['Model'] == dc['Model']]
            tb1_new = tb1.drop([idx[0]])
            tb1_new.to_pickle("./data/tb1.pkl")
        # Из 2 таблицы можно удалять только определенные автосалоны, так как они однозначно определяют телефон
        elif (int(count) == 2):
            idx = tb2.index[tb2['Dealership'] == dc['Dealership']]

            tb2_new = tb2.drop([idx[0]])
            tb2_new.to_pickle("./data/tb2.pkl")
        # Из 3 таблицы можно удалять только те строки, которые соотвествуют марке машины
        elif (int(count) == 3):
            idx = tb3.index[tb3['Brand'] == dc['Brand']]
            tb3_new = tb3.drop([idx[0]])
            tb3_new.to_pickle("./data/tb3.pkl")

    tk.Button(newWindow,
              text='Сохранить изменения в базу данных',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: save_values_del(tb1, tb2, tb3)
              ).place(x=225, y=300)
    btn2 = tk.Button(newWindow, text='Закончить ввод', font=7, bg=stg.knop, activebackground='white',
                     command=newWindow.destroy)
    btn2.place(x=35, y=300)


# Функции добавления в базу данных
def add_car(newWindow: tk.Tk, tb1: pd.DataFrame, tb2: pd.DataFrame, tb3: pd.DataFrame):
    """
    Функция, осуществляющая добавление новой записи в базу данных

    Parameters
    ----------
    newWindow : tk.Tk
        виджет, создающий новое окно
    tb1 : pd.DataFrame
        таблица с моделями машин 
    tb2 : pd.DataFrame
        таблица с телефонами каждого автосалона
    tb3 : pd.DataFrame
        таблица с сувенирами каджой марки машины

    Returns
    -------
        -
        Автор: Букина Валерия

    """
    # Поля ввода для создания данного отчёта
    tk.Label(newWindow, text='Вводите все значения полностью!', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=5)

    b_name = tk.StringVar()
    tk.Label(newWindow, text='Введите марку автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=50)
    tk.Entry(newWindow, textvariable=b_name).place(x=365, y=55)

    m_name = tk.StringVar()
    tk.Label(newWindow, text='Введите модель автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=100)
    tk.Entry(newWindow, textvariable=m_name).place(x=365, y=105)

    price = tk.StringVar()
    tk.Label(newWindow, text='Введите стоимость:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=150)
    tk.Entry(newWindow, textvariable=price).place(x=365, y=155)

    g_name = tk.StringVar()
    tk.Label(newWindow, text='Введите сувенир марки:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=200)
    tk.Entry(newWindow, textvariable=g_name).place(x=365, y=205)

    d_name = tk.StringVar()
    tk.Label(newWindow, text='Введите название автосалона:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=250)
    tk.Entry(newWindow, textvariable=d_name).place(x=365, y=255)

    number = tk.StringVar()
    tk.Label(newWindow, text='Введите номер телефона:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=300)
    tk.Entry(newWindow, textvariable=number).place(x=365, y=305)

    def save_values_add(tb1: pd.DataFrame, tb2: pd.DataFrame, tb3: pd.DataFrame):
        """
        Функция производит добавление определенной информации 
        Если данное изменение таблицы ведёт к изменению других таблиц, то соответсвующие значения будут добавлены во все связанные таблицы
        ----------
        tb1 : pd.DataFrame
            таблица с моделями машин 
        tb2 : pd.DataFrame
            таблица с телефонами каждого автосалона
        tb3 : pd.DataFrame
            таблица с сувенирами каджой марки машины
        Returns
        -------
            -

        Автор: Букина Валерия

        """
        # Создание словаря, хранящего в себе значения новой записи
        dc = {}
        dc['Brand'] = b_name.get()
        dc['Model'] = m_name.get()
        dc['Price'] = price.get()
        dc['Gift'] = g_name.get()
        dc['Dealership'] = d_name.get()
        dc['Telephone'] = number.get()

        if not ((tb1['Model'] == dc['Model']).any()):
            tb1_df = pd.DataFrame({"Brand": [dc['Brand']],
                                   "Model": [dc['Model']],
                                   "Price": [dc['Price']],
                                   "Dealership": [dc['Dealership']]})
            # Сохранение изменений через xlsx; обновление pickle файла
            tb1_new = pd.concat([tb1, tb1_df], ignore_index=True)
            tb1_new.to_excel("./data/tb1.xlsx",index=False)
            f1_new = pd.read_excel("./data/tb1.xlsx")
            f1_new.to_pickle("./data/tb1.pkl")

        if not ((tb2['Dealership'] == dc['Dealership']).any()):
            tb2_df = pd.DataFrame({"Dealership": [dc['Dealership']],
                                   "Telephone": [dc['Telephone']]})
            # Сохранение изменений через xlsx; обновление pickle файла
            tb2_new = pd.concat([tb2, tb2_df], ignore_index=True)
            tb2_new.to_excel("./data/tb2.xlsx",index=False)
            f2_new = pd.read_excel("./data/tb2.xlsx")
            f2_new.to_pickle("./data/tb2.pkl")

        if not ((tb3['Brand'] == dc['Brand']).any()):
            tb3_df = pd.DataFrame({"Brand": [dc['Brand']],
                                   "Gift": [dc['Gift']]})
            # Сохранение изменений через xlsx; обновление pickle файла
            tb3_new = pd.concat([tb3, tb3_df], ignore_index=True)
            tb3_new.to_excel("./data/tb3.xlsx",index=False)
            f3_new = pd.read_excel("./data/tb3.xlsx")
            f3_new.to_pickle("./data/tb3.pkl")

    tk.Button(newWindow,
              text='Сохранить значения в базу данных',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: save_values_add(tb1, tb2, tb3)
              ).place(x=225, y=355)
    btn2 = tk.Button(newWindow, text='Закончить ввод', font=7, bg=stg.knop, activebackground='white',
                     command=newWindow.destroy)
    btn2.place(x=35, y=355)


# Функция редактирования записи в базе данных
def edit_item(newWindow: tk.Tk, tb1: pd.DataFrame, tb2: pd.DataFrame, tb3: pd.DataFrame):
    """
    Функция, осуществляющая редактирование существующих записей

    Parameters
    ----------
    newWindow : tk.Tk
        виджет, создающий новое окно
    tb1 : pd.DataFrame
        таблица с моделями машин 
    tb2 : pd.DataFrame
        таблица с телефонами каждого автосалона
    tb3 : pd.DataFrame
        таблица с сувенирами каджой марки машины

    Returns
    -------
        -
    Автор: Грязева Ксения

    """
    # Поля ввода для изменения данной записи
    c_name = tk.StringVar()
    tk.Label(newWindow, text='Введите номер изменяемой таблицы:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=225)
    tk.Entry(newWindow, textvariable=c_name).place(x=365, y=230)

    def open_necess_table(tb1: pd.DataFrame, tb2: pd.DataFrame, tb3: pd.DataFrame):
        """
        Функция производит добавление определенной информации в существующую запись
        Если данное изменение таблицы ведёт к изменению других таблиц, то соответсвующие значения будут добавлены во все связанные таблицы
        ----------
        tb1 : pd.DataFrame
            таблица с моделями машин 
        tb2 : pd.DataFrame
            таблица с телефонами каждого автосалона
        tb3 : pd.DataFrame
            таблица с сувенирами каджой марки машины

        Returns
        -------
            -

        Автор: Грязева Ксения

        """
        # Создание словаря, хранящего в себе новые значения существующей 
        count = c_name.get()
        name = 'tb' + count
        w = reports.table_by_path("./data/" + name + ".pkl")

        table = ttk.Treeview(newWindow)
        table['columns'] = list(w.columns)
        for column in table['columns']:
            table.heading(column, text=column)
            table.column(column, width=100, anchor=tk.CENTER)
        i = iter(w.index)
        for value in w.values:
            table.insert('', 'end', next(i), values=list(value))
        table.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2)

        # Функция выбирающая строку, которую необходимо изменить
        def choose_value(table: ttk.Treeview, count: str):
            """
            Функция, которая осуществляет выбор изменяемой строки
            и производит изменение
            Parameters
            ----------
            table : ttk.Treeview
                дерево, созданное из текущей базы данных
            count : str
                номер таблицы

            Returns
            -------
                -
            Автор: Грязева Ксения

            """
            selection = table.selection()
            this = table.item(selection)['values']

            # Создание нового окна, где пользователь введёт новые значения
            newWindow1 = tk.Toplevel(newWindow)
            newWindow1['bg'] = stg.fon
            newWindow1.title('Ввод значений редактируемой записи')
            newWindow1.geometry('600x400')

            # Поля для ввода значений
            b_name = tk.StringVar()
            tk.Label(newWindow1, text='Введите марку автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=50)
            tk.Entry(newWindow1, textvariable=b_name).place(x=365, y=55)

            m_name = tk.StringVar()
            tk.Label(newWindow1, text='Введите модель автомобиля:', bg=stg.fon, fg=stg.knop, font=7).place(x=10,
                                                                                                              y=100)
            tk.Entry(newWindow1, textvariable=m_name).place(x=365, y=105)

            price = tk.StringVar()
            tk.Label(newWindow1,text= 'Введите стоимость:',bg=stg.fon,fg=stg.knop,font=7).place(x=10,y=150)
            tk.Entry(newWindow1, textvariable = price).place(x=365,y=155)

            g_name = tk.StringVar()
            tk.Label(newWindow1, text='Введите сувенир марки:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=200)
            tk.Entry(newWindow1, textvariable=g_name).place(x=365, y=205)

            d_name = tk.StringVar()
            tk.Label(newWindow1, text='Введите название автосалона:', bg=stg.fon, fg=stg.knop, font=7).place(x=10,
                                                                                                                y=250)
            tk.Entry(newWindow1, textvariable=d_name).place(x=365, y=255)

            number = tk.StringVar()
            tk.Label(newWindow1, text='Введите номер телефона:', bg=stg.fon, fg=stg.knop, font=7).place(x=10, y=300)
            tk.Entry(newWindow1, textvariable=number).place(x=365, y=305)

            def write_and_save_new_value(this: list, сount: str, tb1: pd.DataFrame, tb2: pd.DataFrame,
                                         tb3: pd.DataFrame):
                """
                Функция записывает и сохраняет новые значения в соответствующие базы данных

                Parameters
                ----------
                this : list
                    текущая выбранная строка в базе данных, которую будем редактировать
                сount : str
                    номер таблицы
                tb1 : pd.DataFrame
                    таблица с моделями машин 
                tb2 : pd.DataFrame
                    таблица с телефонами каждого автосалона
                tb3 : pd.DataFrame
                    таблица с сувенирами каджой марки машины

                Returns
                -------
                    -
                    Автор: Грязева Ксения

                """
                # Словарь с новыми значениями для ячеек таблицы
                dc = {}
                dc['Brand'] = b_name.get()
                dc['Model'] = m_name.get()
                dc['Price'] = price.get()
                dc['Gift'] = g_name.get()
                dc['Dealership'] = d_name.get()
                dc['Telephone'] = number.get()

                tb1_new = tb1
                tb2_new = tb2
                tb3_new = tb3

                # Если для изменения выбрана 1 таблица - Модели
                if (int(count) == 1):
                    idx = tb1.index[tb1['Model'] == this[1]]
                    if (dc['Brand'] != ''):
                        tb1_new.loc[idx, 'Brand'] = dc['Brand']
                    if (dc['Model'] != ''):
                        tb1_new.loc[idx, 'Model'] = dc['Model']
                    if(dc['Price'] != ''):
                        tb1_new.loc[idx,'Price'] = dc['Price']
                    if (dc['Dealership'] != ''):
                        tb1_new.loc[idx, 'Dealership'] = dc['Dealership']
                    # Сохранение изменений через xlsx; обновление pickle файла
                    tb1_new.to_excel("./data/tb1.xlsx",index=False)
                    f1_new = pd.read_excel("./data/tb1.xlsx")
                    f1_new.to_pickle("./data/tb1.pkl")

                # Если для изменения выбрана 2 таблица - Телефоны
                if (int(count) == 2):
                    idx = tb2.index[tb2['Dealership'] == this[0]]
                    if (dc['Dealership'] != ''):
                        tb2_new.loc[idx, 'Dealership'] = dc['Dealership']
                    if (dc['Telephone'] != ''):
                        tb2_new.loc[idx, 'Telephone'] = dc['Telephone']

                # Если для изменения выбрана 3 таблица - Сувениры
                if (int(count) == 3):
                    idx = tb3.index[tb3['Brand'] == this[0]]
                    if (dc['Brand'] != ''):
                        tb3_new.loc[idx, 'Brand'] = dc['Brand']
                    if (dc['Gift'] != ''):
                        tb3_new.loc[idx, 'Gift'] = dc['Gift']

                # Обновление таблиц 
                tb2_new.to_pickle("./data/tb2.pkl")
                tb3_new.to_pickle("./data/tb3.pkl")

                # Кнопка, осуществляющая сохранение введеных изменений 

            tk.Button(newWindow1, text='Сохранить изменения', font=7, bg=stg.knop, activebackground='white',
                      command=lambda: write_and_save_new_value(this, count, tb1, tb2, tb3)).place(x=250, y=360)

            tk.Button(newWindow1, text='Закончить ввод', font=7,
                      bg=stg.knop, activebackground='white', command=newWindow1.destroy).place(x=35, y=355)

        # Кнопка, осуществляющая функцую выбора изменяемого поля    
        tk.Button(newWindow, text='Выберите поле для изменения', font=7, bg=stg.knop, activebackground='white',
                  command=lambda: choose_value(table, count)).place(x=250, y=300)

    # Кнопка, осуществляющая открытие необходимой таблицы
    tk.Button(newWindow,
              text='Открыть нужную таблицу',
              bg=stg.knop,
              activebackground='white',
              font=7,
              command=lambda: open_necess_table(tb1, tb2, tb3)
              ).place(x=225, y=355)
    tk.Button(newWindow, text='Закончить ввод', font=7, bg=stg.knop,
              activebackground='white', command=newWindow.destroy).place(x=35, y=355)