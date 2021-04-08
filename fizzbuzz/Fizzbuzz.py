from tkinter import *

root = Tk()

class App():
    def __init__(self, master):
        self.master = master
        master.title('Fizzbuzz')
        master.geometry('400x400')

        self.num_label = Label(master, text='Enter a number: ')
        self.num_label.pack()

        self.num_entry = Entry(master)
        self.num_entry.pack()

        self.answer = Label(master, text='')
        self.answer.pack()

        self.submit_button = Button(master, text='Submit', command=self.fizzbuzz) 
        self.submit_button.pack()

        #additional
        self.divisor_1_label = Label(master, text='Enter a divisor for fizz: ')
        self.divisor_1_label.pack()

        self.divisor_1_entry = Entry(master)
        self.divisor_1_entry.pack()

        self.divisor_2_label = Label(master, text='Enter a divisor for buzz: ')
        self.divisor_2_label.pack()

        self.divisor_2_entry = Entry(master)
        self.divisor_2_entry.pack()

        self.int_label = Label(master, text='Enter an integer: ')
        self.int_label.pack()

        self.integer_entry = Entry(master)
        self.integer_entry.pack()

        self.replacement_fizzbuzz_label = Label(master, text='Enter a replacement for fizzbuzz: ')
        self.replacement_fizzbuzz_label.pack()

        self.replacement_fizzbuzz_entry = Entry(master)
        self.replacement_fizzbuzz_entry.pack()

        self.replacement_fizz_label = Label(master, text='Enter a replacement for fizz: ')
        self.replacement_fizz_label.pack()

        self.replacement_fizz_entry = Entry(master)
        self.replacement_fizz_entry.pack()

        self.replacement_buzz_label = Label(master, text='Enter a replacement for buzz: ')
        self.replacement_buzz_label.pack()

        self.replacement_buzz_entry = Entry(master)
        self.replacement_buzz_entry.pack()

        self.answer_2 = Label(master, text='')
        self.answer_2.pack()

        self.submit_button_2 = Button(master, text='Submit', command=self.fizzbuzz_with_input) 
        self.submit_button_2.pack()

    def fizzbuzz_with_input(self):
        try:
            try:
                fizzbuzz = self.replacement_fizzbuzz_entry.get()
                if not fizzbuzz:
                    raise ValueError('empty String')
            except ValueError:
                fizzbuzz = 'fizzbuzz'
            try:
                fizz = self.replacement_fizz_entry.get()
                if not fizz:
                    raise ValueError('empty String')
            except ValueError:
                fizz = 'fizz'
            try:
                buzz = self.replacement_buzz_entry.get()
                if not buzz:
                    raise ValueError('empty String')
            except ValueError:
                buzz = 'buzz'
            try:
                fizz_num = int(self.divisor_1_entry.get())
                if not fizz_num:
                    raise ValueError('empty int')
            except ValueError:
                fizz_num = 3
            try:
                buzz_num = int(self.divisor_2_entry.get())
                if not buzz_num:
                    raise ValueError('empty int')
            except ValueError:
                buzz_num = 5

            num_list = []
            for i in range(1, int(self.integer_entry.get())+1):
                if i % fizz_num == 0 and i % buzz_num == 0:
                    num_list.append(fizzbuzz)
                    continue
                elif i % fizz_num == 0:
                    num_list.append(fizz)
                    continue
                elif i % buzz_num == 0:
                    num_list.append(buzz)
                    continue
                num_list.append(i)
            self.answer_2.config(text=num_list)
        except ValueError:
            self.answer_2.config(text='Add an integer!')

    def fizzbuzz(self):        
        try:
            num_list = []
            for fizzbuzz in range(1, int(self.num_entry.get())+1):
                if fizzbuzz % 15 == 0:
                    num_list.append('fizzbuzz')
                    continue
                elif fizzbuzz % 3 == 0:
                    num_list.append('fizz')
                    continue
                elif fizzbuzz % 5 == 0:
                    num_list.append('buzz')
                    continue
                num_list.append(fizzbuzz)
            self.answer.config(text=num_list)
        except ValueError:
            self.answer.config(text='Add an integer!')

a = App(root)
root.mainloop()

    