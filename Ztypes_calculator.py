from tkinter import *                  # импортирование основных функций модуля TKinter
from tkinter import messagebox as m    # импортирование метода для вывода уведомления в отдельном окне

numbers = ''                           # создание переменных, используемых в программе
error_win_name = 'Произошла ошибка'
error = '''Варианты причины проблемы: \nВы начали писать целое число с нуля \nВы разделили на ноль \nВ операции допущена ошибка'''


def make_digit_button(digit):          # объявление функции для создания кнопок с цифрами
    return Button(app, text=digit, font=('Tahoma', 20), bg='#2b2b2b', fg='#ffffff', activebackground='#e8e8e8', command=lambda: print_digit(digit)) #dark


def print_digit(digit):                # объявление функции для ввода цифры
    global numbers

    numbers = '' if numbers.endswith('**2') or numbers.endswith('**0.5') else numbers
    numbers += f'{digit}'
    mylabel.config(text=numbers)


def plus():                            # объявление функции для оператора сложения
    global numbers

    try:
        if numbers:
            numbers = numbers[: -1] if numbers[-1] in '+-*/' else numbers
            numbers = numbers[: -3] if numbers.endswith('**2') else numbers
            numbers = numbers[: -5] if numbers.endswith('**0.5') else numbers
            numbers = str(int(eval(numbers)) if eval(numbers) - int(eval(numbers)) == 0 else eval(numbers))
            numbers += '+'
            mylabel.config(text=numbers)
    except (SyntaxError, ZeroDivisionError):
        m.showinfo(error_win_name, error)


def minus():                           # объявление функции для оператора вычитания
    global numbers

    try:
        if numbers:
            numbers = numbers[: -1] if numbers[-1] in '+-*/' else numbers
            numbers = numbers[: -3] if numbers.endswith('**2') else numbers
            numbers = numbers[: -5] if numbers.endswith('**0.5') else numbers
            numbers = str(int(eval(numbers)) if eval(numbers) - int(eval(numbers)) == 0 else eval(numbers))
            numbers += '-'
            mylabel.config(text=numbers)
    except (SyntaxError, ZeroDivisionError):
        m.showinfo(error_win_name, error)


def multiply():                        # объявление функции для оператора умножения
    global numbers

    try:
        if numbers:
            numbers = numbers[: -1] if numbers[-1] in '+-*/' else numbers
            numbers = numbers[: -3] if numbers.endswith('**2') else numbers
            numbers = numbers[: -5] if numbers.endswith('**0.5') else numbers
            numbers = str(int(eval(numbers)) if eval(numbers) - int(eval(numbers)) == 0 else eval(numbers))
            numbers += '*'
            mylabel.config(text=numbers)
    except (SyntaxError, ZeroDivisionError):
        m.showinfo(error_win_name, error)


def divide():                          # объявление функции для оператора деления
    global numbers

    try:
        if numbers:
            numbers = numbers[: -1] if numbers[-1] in '+-*/' else numbers
            numbers = numbers[: -3] if numbers.endswith('**2') else numbers
            numbers = numbers[: -5] if numbers.endswith('**0.5') else numbers
            numbers = str(int(eval(numbers)) if eval(numbers) - int(eval(numbers)) == 0 else eval(numbers))
            numbers += '/'
            mylabel.config(text=numbers)
    except (SyntaxError, ZeroDivisionError):
        m.showinfo(error_win_name, error)


def square():                          # объявление функции для оператора возведения в квадрат
    global numbers

    try:
        if numbers:
            numbers = numbers[: -1] if numbers[-1] in '+-*/' else numbers
            numbers = numbers[: -3] if numbers.endswith('**2') else numbers
            numbers = numbers[: -5] if numbers.endswith('**0.5') else numbers
            numbers = str(int(eval(numbers)) if eval(numbers) - int(eval(numbers)) == 0 else eval(numbers))
            numbers += '**2'
            mylabel.config(text=numbers)
    except (SyntaxError, ZeroDivisionError):
        m.showinfo(error_win_name, error)


def root():                            # объявление функции для оператора извлечения из корня
    global numbers

    try:
        if numbers:
            numbers = numbers[: -1] if numbers[-1] in '+-*/' else numbers
            numbers = numbers[: -3] if numbers.endswith('**2') else numbers
            numbers = numbers[: -5] if numbers.endswith('**0.5') else numbers
            numbers = str(int(eval(numbers)) if eval(numbers) - int(eval(numbers)) == 0 else eval(numbers))
            numbers += '**0.5'
            mylabel.config(text=numbers)
    except (SyntaxError, ZeroDivisionError):
        m.showinfo(error_win_name, error)


def print_dot():                       # объявление функции для ввода точки
    global numbers

    numbers = '0' if not numbers else numbers
    numbers = numbers + '0' if numbers[-1] in '+-*/' else numbers
    numbers = '0' if numbers.endswith('**2') or numbers.endswith('**0.5') else numbers
    numbers += '.'
    mylabel.config(text=numbers)


def delete():                          # объявление функции для стирания числа или оператора
    global numbers

    if numbers:
        numbers = numbers[:-1]
        mylabel.config(text=numbers)


def clear():                           # объявление функции для очищения поля ввода
    global numbers

    if numbers:
        numbers = ''
        mylabel.config(text=numbers)


def equals():                          # объявление функции для вывода результата
    global numbers

    try:
        if numbers:
            numbers = str(int(eval(numbers)) if eval(numbers) - int(eval(numbers)) == 0 else eval(numbers)) if numbers[-1] \
                not in '+-*/' else numbers[:-1]
            mylabel.config(text=numbers)
    except (SyntaxError, ZeroDivisionError):
        m.showinfo(error_win_name, error)


app_width = 953                        # создание и конфигурация окна приложения
app_height = 509
app = Tk()
app.title("Calculator of Bagir")
app.geometry(f'{app_width}x{app_height}+{app_width}+{app_height}')
app.resizable(False, False)
app.config(bg='#000000')

mylabel = Label(app, text=numbers, bg='#000000', fg='#ffffff', font=('Tahoma', 20), anchor='e', width=62, height=2, padx=10)        # создание поля ввода
mylabel.grid(row=0, column=0, columnspan=4)

make_digit_button(1).grid(row=4, column=0, stick='nswe')     # создание и конфигурация кнопок
make_digit_button(2).grid(row=4, column=1, stick='nswe')
make_digit_button(3).grid(row=4, column=2, stick='nswe')
make_digit_button(4).grid(row=3, column=0, stick='nswe')
make_digit_button(5).grid(row=3, column=1, stick='nswe')
make_digit_button(6).grid(row=3, column=2, stick='nswe')
make_digit_button(7).grid(row=2, column=0, stick='nswe')
make_digit_button(8).grid(row=2, column=1, stick='nswe')
make_digit_button(9).grid(row=2, column=2, stick='nswe')
make_digit_button(0).grid(row=5, column=0, stick='nswe')
Button(app, text='+', bg='#d97f11', fg='#ffffff', activebackground='#ffd5a1', font=('Tahoma', 20), command=plus).grid(row=4, column=3, stick='nswe')          #orange
Button(app, text='-', bg='#2b2b2b', fg='#ffffff', activebackground='#e8e8e8', font=('Tahoma', 20), command=minus).grid(row=5, column=2, stick='nswe')         #dark
Button(app, text='*', bg='#d97f11', fg='#ffffff', activebackground='#ffd5a1', font=('Tahoma', 20), command=multiply).grid(row=3, column=3, stick='nswe')      #orange
Button(app, text='/', bg='#d97f11', fg='#ffffff', activebackground='#ffd5a1', font=('Tahoma', 20), command=divide).grid(row=2, column=3, stick='nswe')        #orange
Button(app, text='sq', bg='#b8b8b8', activebackground='#f2f2f2', font=('Tahoma', 20), command=square).grid(row=1, column=0, stick='nswe')                     #white
Button(app, text='rt', bg='#b8b8b8', activebackground='#f2f2f2', font=('Tahoma', 20), command=root).grid(row=1, column=1, stick='nswe')                       #white
Button(app, text='del', bg='#d97f11', fg='#ffffff', activebackground='#ffd5a1', font=('Tahoma', 20), command=delete).grid(row=1, column=3, stick='nswe')      #orange
Button(app, text=',', bg='#2b2b2b', fg='#ffffff', activebackground='#e8e8e8', font=('Tahoma', 20), command=print_dot).grid(row=5, column=1, stick='nswe')     #dark
Button(app, text='=', bg='#d97f11', fg='#ffffff', activebackground='#ffd5a1', font=('Tahoma', 20), command=equals).grid(row=5, column=3, stick='nswe')        #orange
Button(app, text='C', bg='#b8b8b8', activebackground='#f2f2f2', font=('Tahoma', 20), command=clear).grid(row=1, column=2, stick='nswe')                       #white

for i in range(6):                                          # конфигурация размера кнопок
    app.grid_rowconfigure(i, minsize=85)

app.mainloop()                                              # запуск цикла работы
