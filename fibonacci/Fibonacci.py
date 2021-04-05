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

    def Fibonacci(self):
        try:
            self.a = 0
            self.b = 1
            self.n = int(self.num_entry.get())
            if self.n < 0:
                self.answer.config(text='Incorrect input')
            elif self.n == 1:
                self.answer.config(text=self.b)
            else:
                for i in range(1, self.n):
                    self.c = self.a + self.b
                    self.a = self.b
                    self.b = self.c
                self.answer.config(text=self.b) 
        except ValueError:
            self.answer.config(text='Incorrect input')

    
a = App(root)
root.mainloop()

    