from tkinter import *

root = Tk()

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        master.title('Combo')
        master.geometry('400x500')

        #fibonacci
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

        self.answer = Label(master, text='')
        self.answer.pack()

        self.submit_button = Button(master, text='Get Fibonacci', command=self.Fibonacci_with_input) 
        self.submit_button.pack()

        #fizzbuzz

        self.divisor_1_label = Label(master, text='Enter a divisor for fizz: ')
        self.divisor_1_label.pack()

        self.divisor_1_entry = Entry(master)
        self.divisor_1_entry.pack()

        self.divisor_2_label = Label(master, text='Enter a divisor for buzz: ')
        self.divisor_2_label.pack()

        self.divisor_2_entry = Entry(master)
        self.divisor_2_entry.pack()

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

        self.submit_button_2 = Button(master, text='Get Fizzbuzz', command=self.fizzbuzz_with_input_from_fibonacci) 
        self.submit_button_2.pack()


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
            global num_list
            num_list = []
            # check if the number of terms is valid
            if int(self.integer_entry.get()) <= 0:
                self.answer.config(text="1")
            elif int(self.integer_entry.get()) == 1:
                num_list.append(self.n1)
            else:
                while self.count <= int(self.integer_entry.get())-1:
                    num_list.append(self.n1)
                    self.nth = self.n1 + self.n2
                    # update values
                    self.n1 = self.n2
                    self.n2 = self.nth
                    self.count += 1
            self.answer.config(text=num_list)
        except ValueError:
            self.answer.config(text='Enter Integer')

    def fizzbuzz_with_input_from_fibonacci(self):
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
            except ValueError:
                fizz_num = 3
            try:
                buzz_num = int(self.divisor_2_entry.get())
            except ValueError:
                buzz_num = 5

            fizzbuzz_list = []
            global num_list
            for i in num_list:
                if i % fizz_num == 0 and i % buzz_num == 0:
                    fizzbuzz_list.append(fizzbuzz)
                    continue
                elif i % fizz_num == 0:
                    fizzbuzz_list.append(fizz)
                    continue
                elif i % buzz_num == 0:
                    fizzbuzz_list.append(buzz)
                    continue
                fizzbuzz_list.append(i)
            self.answer_2.config(text=fizzbuzz_list)
        except NameError:
            self.answer_2.config(text='Enter Fibonacci ')

if __name__ == "__main__":
    a = App(root)
    root.mainloop()

    