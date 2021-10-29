import tkinter as tk
from tkinter import *


class Calculator(tk.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.place()

        self.create_frame_and_listbox()
        self.create_button()

        self.expression = ''

    def choose(self, char):
        self.expression += str(char)
        self.display_calculation.delete(1.0, 'end')
        self.display_calculation.insert(1.0, self.expression)

    def compute(self):
        try:
            self.total = str(eval(self.expression))
            self.display_calculation.delete(1.0, 'end')
            self.display_calculation.insert(1.0, self.total)
        except:
            self.clear()
            self.display_calculation.insert(1.0, 'Error')

    def clear(self):
        self.expression = ''
        self.display_calculation.delete(1.0, 'end')
        self.display_calculation.insert(1.0, 0)

    def create_frame_and_listbox(self):
        self.calculation_frame = Frame(root, width=235, height=120, bg="Black", bd=10, relief=SUNKEN)
        self.calculation_frame.place(x=10, y=0)

        self.display_calculation = Text(self.calculation_frame, bg='Black', fg='White',
                                        font=('Courier', 15, 'bold'))
        self.display_calculation.place(x=0, y=0, width=215, height=100)
        self.display_calculation.insert(1.0, 0)

    def create_button(self):
        self.button_division = Button(root, text='÷', font=('Courier', 15, 'bold'), bg='orange3',
                                      fg="White", width=3, command=lambda: self.choose('/'))
        self.button_division.place(x=200, y=130)
        self.button_division.config(activebackground="orange4", relief=RAISED)

        self.button_multiplication = Button(root, text='x', font=('Courier', 15, 'bold'),
                                            bg='orange3', fg="White", width=3,
                                            command=lambda: self.choose('*'))
        self.button_multiplication.place(x=200, y=190)
        self.button_multiplication.config(activebackground="orange4", relief=RAISED)

        self.button_soustraction = Button(root, text='-', font=('Courier', 15, 'bold'), bg='orange3',
                                          fg="White", width=3,
                                          command=lambda: self.choose('-'))
        self.button_soustraction.place(x=200, y=250)
        self.button_soustraction.config(activebackground="orange4", relief=RAISED)

        self.button_addition = Button(root, text='+', font=('Courier', 15, 'bold'), bg='orange3',
                                      fg="White", width=3, command=lambda: self.choose('+'))
        self.button_addition.place(x=200, y=310)
        self.button_addition.config(activebackground="orange4", relief=RAISED)

        self.button_egal = Button(root, text='=', font=('Courier', 15, 'bold'), bg='orange3',
                                  fg="White", width=3, command=self.compute)
        self.button_egal.place(x=200, y=370)
        self.button_egal.config(activebackground="orange4", relief=RAISED)

        self.button_zero = Button(root, text='0', font=('Courier', 15, 'bold'), bg='gray15',
                                  fg="White", width=8,
                                  command=lambda: self.choose(0))
        self.button_zero.place(x=10, y=370)
        self.button_zero.config(activebackground="gray50", relief=RAISED)

        self.button_point = Button(root, text='.', font=('Courier', 15, 'bold'), bg='gray15',
                                   fg="White", width=3, command=lambda: self.choose('.'))
        self.button_point.place(x=130, y=370)
        self.button_point.config(activebackground="gray50", relief=RAISED)

        self.button_one = Button(root, text='1', font=('Courier', 15, 'bold'), bg='gray15',
                                 fg="White", width=3, command=lambda: self.choose(1))
        self.button_one.place(x=10, y=310)
        self.button_one.config(activebackground="gray50", relief=RAISED)

        self.button_two = Button(root, text='2', font=('Courier', 15, 'bold'), bg='gray15',
                                 fg="White", width=3, command=lambda: self.choose(2))
        self.button_two.place(x=70, y=310)
        self.button_two.config(activebackground="gray50", relief=RAISED)

        self.button_three = Button(root, text='3', font=('Courier', 15, 'bold'), bg='gray15',
                                   fg="White", width=3, command=lambda: self.choose(3))
        self.button_three.place(x=130, y=310)
        self.button_three.config(activebackground="gray50", relief=RAISED)

        self.button_four = Button(root, text='4', font=('Courier', 15, 'bold'), bg='gray15',
                                  fg="White", width=3, command=lambda: self.choose(4))
        self.button_four.place(x=10, y=250)
        self.button_four.config(activebackground="gray50", relief=RAISED)

        self.button_five = Button(root, text='5', font=('Courier', 15, 'bold'), bg='gray15',
                                  fg="White", width=3, command=lambda: self.choose(5))
        self.button_five.place(x=70, y=250)
        self.button_five.config(activebackground="gray50", relief=RAISED)

        self.button_six = Button(root, text='6', font=('Courier', 15, 'bold'), bg='gray15',
                                 fg="White", width=3, command=lambda: self.choose(6))
        self.button_six.place(x=130, y=250)
        self.button_six.config(activebackground="gray50", relief=RAISED)

        self.button_seven = Button(root, text='7', font=('Courier', 15, 'bold'), bg='gray15',
                                   fg="White", width=3, command=lambda: self.choose(7))
        self.button_seven.place(x=10, y=190)
        self.button_seven.config(activebackground="gray50", relief=RAISED)

        self.button_eight = Button(root, text='8', font=('Courier', 15, 'bold'), bg='gray15',
                                   fg="White", width=3, command=lambda: self.choose(8))
        self.button_eight.place(x=70, y=190)
        self.button_eight.config(activebackground="gray50", relief=RAISED)

        self.button_nine = Button(root, text='9', font=('Courier', 15, 'bold'), bg='gray15',
                                  fg="White", width=3, command=lambda: self.choose(9))
        self.button_nine.place(x=130, y=190)
        self.button_nine.config(activebackground="gray50", relief=RAISED)

        self.button_clear = Button(root, text='C', font=('Courier', 15, 'bold'), bg='gray60',
                                   fg="Black", width=3, command=self.clear)
        self.button_clear.place(x=10, y=130)
        self.button_clear.config(activebackground="gray75", relief=RAISED)

        self.button_plus_or_less = Button(root, text='+/-', font=('Courier', 15, 'bold'), bg='gray60',
                                          fg="Black", width=3, command=lambda: self.choose('-'))
        self.button_plus_or_less.place(x=70, y=130)
        self.button_plus_or_less.config(activebackground="gray75", relief=RAISED)

        self.button_modulo = Button(root, text='%', font=('Courier', 15, 'bold'), bg='gray60',
                                    fg="Black", width=3, command=lambda: self.choose('%'))
        self.button_modulo.place(x=130, y=130)
        self.button_modulo.config(activebackground="gray75", relief=RAISED)


root = Tk()
root.geometry("255x420+355+30")
root.resizable(False, False)
root.title('Simple Calculator')
root.iconbitmap('icon.ico')
root.config(background="black")

app = Calculator(master=root)
app.mainloop()
