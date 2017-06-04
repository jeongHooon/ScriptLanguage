from tkinter import *

def start():
    window = Tk()
    button1 = Button(window, text="발행정보 조회")
    button1.grid(row=0,column=0)
    button2 = Button(window, text="기업정보 조회")
    button2.grid(row=1,column=0)
    button3 = Button(window, text="주식정보 조회")
    button3.grid(row=2,column=0)
    button4 = Button(window, text="금융용어 조회")
    button4.grid(row=3,column=0)
    window.mainloop()