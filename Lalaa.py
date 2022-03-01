from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Online doctor(kinda)")
root.geometry("300x300")

q1r = StringVar(value="0")

q1lbl = Label(root,text = "Do you have Headache?")
q1lbl.pack()

rb11 = Radiobutton(root , text="yes" , variable = q1r , value = "yes")
rb11.pack()

rb12 = Radiobutton(root , text="no" , variable = q1r , value = "no")
rb12.pack()

q2r = StringVar(value="0")

q2lbl = Label(root,text = "Is you body temperature greater than 98.6°?")
q2lbl.pack()

rb21 = Radiobutton(root , text="yes" , variable = q2r , value = "yes")
rb21.pack()

rb22 = Radiobutton(root , text="no" , variable = q2r , value = "no")
rb22.pack()

q3r = StringVar(value="0")

q3lbl = Label(root,text = "Did you vomit frequently?")
q3lbl.pack()

rb31 = Radiobutton(root , text="yes" , variable = q3r , value = "yes")
rb31.pack()

rb32 = Radiobutton(root , text="no" , variable = q3r , value = "no")
rb32.pack()


def sCoReFeVeR() :
    sCoRe = 0
    if q1r.get() == "yes":
        sCoRe = sCoRe + 10
        print(sCoRe)
    if q2r.get() == "yes":
        sCoRe = sCoRe + 10
        print(sCoRe)
    if q3r.get() == "yes":
        sCoRe = sCoRe + 10
        print(sCoRe)


    if sCoRe <= 10:
        messagebox.showinfo("No need to worry","You don't need to visit a doctor")
    elif sCoRe > 10 and sCoRe <= 20:
        messagebox.showwarning("Info","You might need to visit a doctor")
    else:
        messagebox.showerror("WARNING!!","Strongly advise you to meet a doctor")


BtNnN = Button(root , text="check results" , command = sCoReFeVeR)
BtNnN.pack()

root.mainloop()

