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

        self.answer_2 = Label(master, text='')
        self.answer_2.pack()

        self.submit_button_2 = Button(master, text='Submit', command=self.fizzbuzz_with_input) 
        self.submit_button_2.pack()

    def fizzbuzz_with_input(self):
        try:
            num_list = []
            for fizzbuzz in range(1, int(self.integer_entry.get())+1):
                fizz = int(self.divisor_1_entry.get())
                buzz = int(self.divisor_2_entry.get())
                if fizzbuzz % fizz == 0 and fizzbuzz % buzz == 0:
                    num_list.append('fizzbuzz')
                    continue
                elif fizzbuzz % fizz == 0:
                    num_list.append('fizz')
                    continue
                elif fizzbuzz % buzz == 0:
                    num_list.append('buzz')
                    continue
                num_list.append(fizzbuzz)
            self.answer_2.config(text=num_list)
        except ValueError:
            self.answer_2.config(text='That is not what we are looking for...')

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
            self.answer.config(text='That is not what we are looking for...')

a = App(root)
root.mainloop()

    