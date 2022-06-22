"""
Главный модуль
"""
import tkinter as tk
from tkinter.ttk import Combobox
import os
import sys
sys.path.append("d:/work")
import pandas as pd
import func_db
import reports
from library import settings as stg

os.chdir("d:/work/")

root = tk.Tk()

root['bg'] = stg.fon
root.title('Анализ вторичного рынка иномарок в России')
root.geometry('1000x550')

root.resizable(width=True, height=True)

def spravka(root: tk.Tk):
    """
    Функция, создающая окно со справкой о программе

    Parameters
    ----------
    root : tk.Tk
        новый виджет окна

    Returns
    -------
        -
        Автор: Мартинич Андрей

    """
    new_window = tk.Toplevel(root)
    new_window.title('Справка')
    new_window.geometry('300x300')
    tk.Label(new_window,font = 7, text='Разработчики:\n'+'Букина Валерия\n'+'Грязева Ксения\n'+'Мартинич Андрей\n'+'3 бригада, группа БИВ213\n\n'+'Руководитель:\n'+'Поляков Константин Львович\n\n'+'МИЭМ НИУ ВШЭ\n 2022',anchor = tk.CENTER).pack()

# Создаем объект класса Menu
mainmenu = tk.Menu(root, tearoff=0)  

mainmenu.add_command(label="Справка", command=lambda:spravka(root))
mainmenu.add_command(label="Выход", command=root.destroy)

root.config(menu=mainmenu)


# Функция добавления новой записи в базу данных автомобилей
def add_info():
    """
    Добавление новой записи в базу данных

    Returns
    -------
        -

    Автор: Букина Валерия
    """
    new_window = tk.Toplevel(root)
    new_window['bg'] = stg.fon
    new_window.title('Введите информацию о новой записи')
    new_window.geometry('600x400')
    tb1 = reports.table_by_path("./data/tb1.pkl")
    tb2 = reports.table_by_path("./data/tb2.pkl")
    tb3 = reports.table_by_path("./data/tb3.pkl")

    func_db.add_car(new_window, tb1, tb2, tb3)


# Функция удаления записи из базы данных
def delete_from_table():
    """
    Удаляет выбранную запись из базы данных

    Returns
    -------
        -
    Автор: Мартинич Андрей

    """
    new_window = tk.Toplevel(root)
    new_window['bg'] = stg.fon
    new_window.title('Введите информацию для удаления записи')
    new_window.geometry('600x350')
    tb1 = reports.table_by_path("./data/tb1.pkl")
    tb2 = reports.table_by_path("./data/tb2.pkl")
    tb3 = reports.table_by_path("./data/tb3.pkl")

    func_db.delete_item(new_window, tb1, tb2, tb3)


# Функция редактирования записи в базе данных
def edit_from_table():
    """
    Функция редактирует выбранную запись в базе данных

    Returns
    -------
        -
    Автор: Грязева Ксения
    """
    new_window = tk.Toplevel(root)
    new_window['bg'] = stg.fon
    new_window.title('Введите информацию для редактирования записи')
    new_window.geometry('600x400')
    tb1 = reports.table_by_path("./data/tb1.pkl")
    tb2 = reports.table_by_path("./data/tb2.pkl")
    tb3 = reports.table_by_path("./data/tb3.pkl")

    func_db.edit_item(new_window, tb1, tb2, tb3)


# лэйблы на главном экране
label_help = tk.Label(root,
                      bg=stg.fon,
                      text='Выберите список для отображения:',
                      font=(10),
                      fg=stg.knop
                      )
label_help.place(x=100, y=150)

label_report = tk.Label(root,
                        bg= stg.fon,
                        text='Выберите небходимый отчет:',
                        font=(10),
                        fg=stg.knop
                        )
label_report.place(x=680, y=70)

# Создание и размещение кнопки
del_btn = tk.Button(root, text='Удалить запись',
                    bg=stg.knop,
                    activebackground='white',
                    font=1,
                    command= lambda:delete_from_table()
                    )
del_btn.place(x=140, y=20)

add_btn = tk.Button(root, text='Добавить запись',
                    bg=stg.knop,
                    activebackground='white',
                    font=7,
                    command=lambda:add_info())

add_btn.place(x=134, y=65)
edit_btn = tk.Button(root, text='Редактировать запись',
                     bg=stg.knop,
                     activebackground='white',
                     font=7,
                     command=lambda:edit_from_table()
                     )
edit_btn.place(x=110, y=110)

full_table_btn = tk.Button(root, text='Полный список',
                           bg=stg.knop,
                           activebackground='white',
                           font=7,
                           command=lambda: func_db.print_all(
                               func_db.make_table(pd.read_pickle("./data/tb1.pkl"),
                                                        pd.read_pickle("./data/tb2.pkl"),
                                                        pd.read_pickle("./data/tb3.pkl")), root))
full_table_btn.place(x=10, y=185)

dealership_btn = tk.Button(root, text='Модели-1',
                           bg=stg.knop,
                           font=7,
                           activebackground='white',
                           command=lambda: func_db.print_all(pd.read_pickle("./data/tb1.pkl"), root)
                           )
dealership_btn.place(x=170, y=185)

gifts_btn = tk.Button(root, text='Сувениры-3',
                      bg=stg.knop,
                      activebackground='white',
                      font=7,
                      command=lambda: func_db.print_all(pd.read_pickle("./data/tb3.pkl"), root)
                      )
gifts_btn.place(x=440, y=185)

phones_btn = tk.Button(root, text='Телефоны-2',
                       bg=stg.knop,
                       activebackground='white',
                       font=7,
                       command=lambda: func_db.print_all(pd.read_pickle("./data/tb2.pkl"), root)
                       )
phones_btn.place(x=295, y=185)


# Текстовые отчёты и сводные таблицы
def create_new_window(combo: Combobox):
    """
    Функция создает новое окно на основе выбранного вида отчета

    Parameters
    ----------
    combo : Combobox
        виджет, позволяющий осуществить выбор отчета

    Returns
    -------
        -
    Автор: Грязева Ксения

    """
    choosen = combo.get()
    new_window = tk.Toplevel(root)
    new_window['bg'] = stg.fon
    new_window.title(choosen)
    new_window.geometry('900x500')
    # Создание необходимых для отчетов таблиц
    tb1 = reports.table_by_path("./data/tb1.pkl")
    tb2 = reports.table_by_path("./data/tb2.pkl")
    tb3 = reports.table_by_path("./data/tb3.pkl")
    tb4 = pd.merge(tb1, tb3)
    tb5 = pd.merge(tb1, tb2)

    if choosen == "Текстовый отчет 1":
        reports.text_rep_1(new_window, tb1)
    if choosen == "Текстовый отчет 2":
        reports.text_rep_2(new_window, tb4)
    if choosen == "Текстовый отчет 3":
        reports.text_rep_3(new_window, tb4)
    if choosen == "Сводная таблица 1":
        reports.piv_rep_1(new_window, tb4)
    if choosen == "Сводная таблица 2":
        reports.piv_rep_2(new_window, tb1)
    if choosen == "Сводная таблица 3":
        reports.piv_rep_3(new_window, tb5)
    if choosen == "Графический отчет - сувениры":
        new_window.destroy()
        reports.graph_report_scatter(tb3)
    if choosen == "Графический отчет - средняя стоимость":
        new_window.destroy()
        reports.graph_report_bar(tb1)
    if choosen == "Графический отчет - количество машин":
        new_window.destroy()
        reports.graph_report_hist(tb1)
    if choosen == "Графический отчет-цена машин в автосалоне":
        reports.graph_report_box(new_window, tb1)
    # кнопка для закрытия окна
    btn2 = tk.Button(new_window,
                     text='Закончить ввод',
                     font=7, bg=stg.knop,
                     activebackground='white',
                     command=new_window.destroy)
    btn2.place(x=690, y=460)

# список текстовых отчётов на выбор
combo_list = Combobox(root, values=("Текстовый отчет 1",
                                    "Текстовый отчет 2",
                                    "Текстовый отчет 3",
                                    "Сводная таблица 1",
                                    "Сводная таблица 2",
                                    "Сводная таблица 3",
                                    "Графический отчет - сувениры",
                                    "Графический отчет - средняя стоимость",
                                    "Графический отчет - количество машин",
                                    "Графический отчет-цена машин в автосалоне"),
                              font=20)
combo_list.current(0)
combo_list.place(x=700, y=100)

# Кнопка для создания нового отчёта
analyze_btn = tk.Button(root,
                        text='Создать отчет',
                        font=10,
                        bg=stg.knop,
                        command=lambda: create_new_window(combo_list))
analyze_btn.place(x=740, y=160)


root.mainloop()
