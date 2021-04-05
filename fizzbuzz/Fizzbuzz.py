from tkinter import *

root = Tk()

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
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
            self.answer.config(text='That is not an integer')
    
a = App(root)
root.mainloop()

    