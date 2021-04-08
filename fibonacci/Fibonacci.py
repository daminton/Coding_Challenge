from tkinter import *

root = Tk()

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        master.title('Fibonacci')
        master.geometry('400x400')

        self.num_label = Label(master, text='Enter a number: ')
        self.num_label.pack()

        self.num_entry = Entry(master)
        self.num_entry.pack()

        self.answer = Label(master, text='')
        self.answer.pack()

        self.submit_button = Button(master, text='Submit', command=self.Fibonacci) 
        self.submit_button.pack()

        #additional
        self.num_1_label = Label(master, text='Enter a number for y: ')
        self.num_1_label.pack()

        self.num_1_entry = Entry(master)
        self.num_1_entry.pack()

        self.num_2_label = Label(master, text='Enter a divisor for z: ')
        self.num_2_label.pack()

        self.num_2_entry = Entry(master)
        self.num_2_entry.pack()

        self.int_label = Label(master, text='Enter an integer: ')
        self.int_label.pack()

        self.integer_entry = Entry(master)
        self.integer_entry.pack()

        self.answer_2 = Label(master, text='')
        self.answer_2.pack()

        self.submit_button_2 = Button(master, text='Submit', command=self.Fibonacci_with_input) 
        self.submit_button_2.pack()

    def Fibonacci(self):
        try:
            # first two terms
            self.n1, self.n2 = 1, 1
            self.count = 0
            self.num_list = []
            # check if the number of terms is valid
            if int(self.num_entry.get()) <= 0:
                self.answer.config(text="Please enter a positive integer")
            elif int(self.num_entry.get()) == 1:
                self.num_list.append(self.n1)
            else:
                while self.count < int(self.num_entry.get()):
                    self.num_list.append(self.n1)
                    self.nth = self.n1 + self.n2
                    # update values
                    self.n1 = self.n2
                    self.n2 = self.nth
                    self.count += 1
            self.answer.config(text=self.num_list)
        except ValueError:
            self.answer.config(text='Incorrect input')

    def Fibonacci_with_input(self):
        try:
            # first two terms
            try:
                self.n1 = int(self.num_1_entry.get())
            except ValueError:
                self.n1 = 1
            try:
                self.n2 = int(self.num_2_entry.get())
            except ValueError:
                self.n2 = 1
            self.count = 0
            self.num_list = []
            # check if the number of terms is valid
            if int(self.integer_entry.get()) <= 0:
                self.answer_2.config(text="Please enter a positive integer")
            elif int(self.integer_entry.get()) == 1:
                self.num_list.append(self.n1)
            else:
                while self.count < int(self.integer_entry.get()):
                    self.num_list.append(self.n1)
                    self.nth = self.n1 + self.n2
                    # update values
                    self.n1 = self.n2
                    self.n2 = self.nth
                    self.count += 1
            self.answer_2.config(text=self.num_list)
        except ValueError:
            self.answer_2.config(text='Incorrect input')

    
a = App(root)
root.mainloop()

    