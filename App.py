from tkinter import Tk, Frame, Label, Button, Entry
from tkinter import messagebox
from tkinter import ttk
import time
from datetime import datetime


class Clock:
    def __init__(self, master):
        my_notebook = ttk.Notebook(master)
        my_notebook.pack(pady=10)

        # creating tabs
        my_frame1 = Frame(my_notebook, width=500, height=1000)
        my_frame2 = Frame(my_notebook, width=500, height=700)
        my_frame3 = Frame(my_notebook, width=500, height=700)
        
        my_frame1.pack(fill='both', expand=1)
        my_frame2.pack(fill='both', expand=1)
        my_frame3.pack(fill='both', expand=1)

        my_notebook.add(my_frame1, text='Clock')
        my_notebook.add(my_frame2, text='Stopwatch')
        my_notebook.add(my_frame3, text='Timer')

        self.firstFrame(master, my_frame1)
        self.secondFrame(master, my_frame2)
        self.thirdFrame(master, my_frame3)


    def firstFrame(self, master, my_frame1):
        #def clockUpdate():
        #    while True:
        def keepUpdating():
            x = time.time() + (6*3600)
            current_time = time.strftime('%H:%M:%S', time.gmtime(x))
            my_label = Label(my_frame1, text=current_time, font='Times 50')
            my_label.grid(row=0, column=0, pady=60, padx=110)
            my_label.after(1000, keepUpdating)

        keepUpdating()
    
    def secondFrame(self, master, my_frame2):

        def clearLabel():
            label = Label(my_frame2, text='00:00:00', font='Times 50')
            label.grid(row=0, column=0, pady=60, padx=90)
            start_button.configure(text='Start', command=transition)

        def ZaWarudo():
            first_label.after_cancel(solve)
            start_button.configure(text='Clear', command=clearLabel)
            #first_label['text'] = '00:00:00'
            


        def startWatch():
            finish = time.perf_counter()
            x = round(finish - start)
            elapsed_time = time.strftime('%H:%M:%S', time.gmtime(x))
            first_label = Label(my_frame2, text=elapsed_time, font='Times 50')
            first_label.grid(row=0, column=0, pady=60, padx=100)
            global solve
            solve = first_label.after(1000, startWatch)
        
        def watch():
            global start
            start = time.perf_counter()
            startWatch()
        
        
        def transition():
            start_button.configure(text='Stop', command=ZaWarudo)
            watch()


        
        
        first_label = Label(my_frame2, text='00:00:00', font='Times 50')
        first_label.grid(row=0, column=0, pady=60, padx=90)

        start_button = Button(my_frame2, text='Start', font='Times 24', command=transition)
        start_button.grid(row=1, column=0, pady=60, padx=100, ipadx=100)

        
    def thirdFrame(self, master, my_frame3):

        def checkBox():
            if str(entry_box.get()).isdigit():

                def startTimer(num):
                    remaining_time = time.strftime('%H:%M:%S', time.gmtime(num))
                    main_label['text'] = remaining_time
                    if num>0:
                        main_label.after(1000, startTimer, num - 1) 
                
                num = int(entry_box.get())
                startTimer(num)
            else:
                alert()

        main_label = Label(my_frame3, text='00:00:00', font='Times 50')
        main_label.grid(row=0, column=0, pady=60, padx=120)

        # entry box to enter the number
        entry_box = Entry(my_frame3)
        entry_box.grid(row=1, column=0, pady=30)

        enter_button = Button(my_frame3, text='Start', command=checkBox)
        enter_button.grid(row=2, column=0, pady=10)
      
def alert():
    pass

def main():
    root = Tk()
    root.geometry('500x700')
    app = Clock(root)
    root.mainloop()

if __name__ == '__main__':
    main()