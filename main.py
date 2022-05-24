from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
root = Tk()


root['bg'] = '#2A4D59'
root.title('Машинки')
root.geometry('1000x800')
mainmenu = Menu(root)

root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Файл",
                     menu=filemenu)
mainmenu.add_cascade(label="Справка",
                     menu=helpmenu)
#
root.resizable(width=True, height=True)
# создание иконки
#icon = PhotoImage(file='the met.png')
#root.iconphoto(False, icon)

#
label_help = Label(root,
                   bg='#2A4D59',
                   text='Выберите список для отображения:',
                   font=(10),
                   fg='#7DD2EC'
                   )
label_help.place(x=100, y=150)

label_report = Label(root,
                   bg='#2A4D59',
                   text='Выберите небходимый отчёт:',
                   font=(10),
                   fg='#7DD2EC'
                   )
label_report.place(x=680, y=70)
# Создание и размещение кнопки
del_btn = Button(root, text='Удалить запись',
             bg='#7DD2EC',
             activebackground='white',
            font = 1
             #command=btn_click)
             )
del_btn.place(x=140, y=20)

add_btn = Button(root, text='Добавить запись',
             bg='#7DD2EC',
             activebackground='white',
             font= 7
             #command=btn_click)
             )
add_btn.place(x=134, y=65)
edit_btn = Button(root, text='Редактировать запись',
             bg='#7DD2EC',
             activebackground='white',
             font=7
             #command=btn_click)
             )
edit_btn.place(x=110, y=110)
full_table_btn= Button(root, text='Полный список',
             bg='#7DD2EC',
             activebackground='white',
             font=7
             #command=btn_click)
             )
full_table_btn.place(x=10, y=185)
dealership_btn = Button(root, text='Автосалоны',
             bg='#7DD2EC',
            font=7,
             activebackground='white',
             #command=btn_click)
             )
dealership_btn.place(x=170, y=185)
gifts_btn = Button(root, text='Сувениры',
             bg='#7DD2EC',
             activebackground='white',
             font=7
             #command=btn_click)
             )
gifts_btn.place(x=305, y=185)
phones_btn = Button(root, text='Телефоны',
             bg='#7DD2EC',
             activebackground='white',
             font=7
             #command=btn_click)
             )
phones_btn.place(x=420, y=185)

#combobox
def createNewWindow():
    newWindow = Toplevel(root)
    newWindow['bg'] = '#2A4D59'
    newWindow.title('Текстовый отчёт 3')
    newWindow.geometry('900x500')
    save_btn = Button(newWindow, text='Сохранить отчёт',
                        bg='#7DD2EC',
                        activebackground='white',
                        font=7
                        # command=btn_click)
                        )
    save_btn.place(x=400, y=405)
    base = Text(newWindow,
                wrap=WORD,
                width=110)
    base.place(x=10, y=10)


list_of_functions = Combobox(root,
                             values=("Текстовый отчёт 1",
                                     "Текстовый отчет 2",
                                     "Текстовый отчёт 3",
                                     "Сводная таблица 1",
                                     "Сводная таблица 2",
                                     "Сводная таблица 3"),
                             font=20)
list_of_functions.place(x=700,y=100)
analyze_btn =Button(root,
                    text='Создать отчёт',
                    font=10,
                    bg='#7DD2EC',
                    command=createNewWindow)
analyze_btn.place(x=740,y=160)

#label, где будет показана таблица бд
base = Text(root,
            wrap=WORD,
            width=800,
            height=500)
base.place(x=10,y=250)

root.mainloop()
