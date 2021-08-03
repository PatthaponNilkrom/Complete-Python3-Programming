from tkinter import *
import math

def leftClickButton(event):
    x=float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    if x<18.5:
        labelResult.configure(text="ผอมเกินไป")
    elif x<22.9:
        labelResult.configure(text="น้ำหนักปกติ")
    elif x<24.9:
        labelResult.configure(text="น้ำหนักเกิน")
    elif x<29.9:
        labelResult.configure(text="อ้วน")
    elif x>=30:
        labelResult.configure(text="อ้วนมาก")
    labelNumberResult.configure(text=x)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)",font=("Angsana New",20))
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)",font=("Angsana New",20))
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ",font=("Angsana New",20))
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์",font=("Angsana New",15))
labelResult.grid(row=2,column=1)
labelNumberResult=Label(MainWindow,text="Body Mass Index",font=("Angsana New",15))
labelNumberResult.grid(row=3,column=1)

MainWindow.mainloop()