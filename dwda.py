
from tkinter import *

root=Tk()
root.title("Fibonacci")
root.geometry("500x500")
enter_number=Entry(root)
label1=Label(root, text="Fibonacci series: ")
label2=Label(root, text="Fibonacci sum: ")
def Fibonacci():
    input=int(enter_number.get())
    first_number=0
    second_number=1
    SUM=0
    COUNTER=1
    SUM2=0
    while(counter<=input):
        label1["text"]+=str(sum)+" "
        label2["text"]="Fibonacci sum: "+str(sum2)
        counter=counter+1
        first_number=second_number
        second_number=SUM
        SUM=first_number+second_number
        SUM2=SUM2+SUM
enter_number.pack()
btn=Button(root, text="show fibonacci series", command=Fibonacci)
