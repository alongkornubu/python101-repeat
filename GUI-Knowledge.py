from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี', text)

FB1 = Frame(GUI)
FB1.place(x=100, y=80)

B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
#####################################

def Button3():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี', text)

FB2 = Frame(GUI)
FB2.place(x=100, y=180)

B3 = ttk.Button(FB2,text='เงินมีอยู่กี่บาท',command=Button2)
B3.pack(ipadx=20,ipady=20)


GUI.mainloop()