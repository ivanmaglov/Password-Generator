import random
from tkinter import Button, Label, Entry, Tk, messagebox, StringVar, IntVar, END

root=Tk()
root.title('Password Generator')
root.geometry()
root.resizable(False, False)

name=StringVar()
pass_leng=StringVar()

def generate_pass():
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    chars="@#%&()\"?!"
    numbers='1234567890'
    upper=list(upper)
    lower=list(lower)
    numbers=list(numbers)
    chars=list(chars)
    name2=name.get()
    pass_leng2=pass_leng.get()

    if name2=="":
        messagebox.showwarning("Oops","Name field can't be empty!")
        entrynickname.delete(0,25)
        return

    if len(name2)<4:
        messagebox.showwarning("Warning","Length must be an integer >= 6!")
        entrynickname.delete(0, 25)
        return

    if pass_leng2=="":
        messagebox.showwarning("Oops", "Length field cannot be empty!")
        return

    length = int(pass_leng2)

    if length<6:
        print(length)
        messagebox.showwarning("Opps", "Password must be at least 6 characters long!!!")
        return

    entrygenerated.delete(0,length)

    up=random.randint(1,length-3)
    lo=random.randint(1,length-2-up)
    cha=random.randint(1,length-up-lo)
    num=length-up-lo-cha

    password=random.sample(upper,up)+random.sample(lower,lo)+random.sample(chars,cha)+random.sample(numbers,num)
    random.shuffle(password)
    gen_passwd="".join(password)
    entrygenerated.insert(0,gen_passwd)

def reset():
    name.set("")
    pass_leng.set("")
    entrygenerated.delete(0,25)

lblnickname = Label(root, width=30, text='Enter your nickname or email:', font=('arial 20 bold'),
                        bg='light goldenrod yellow')
lblnickname.grid(row=0, column=0)

entrynickname = Entry(root, width=35, font=('arial 20 bold'), bg='white', textvariable=name)
entrynickname.grid(row=0, column=1)
entrynickname.focus_set()

lbllength = Label(root, width=30, text='Enter the lenght of your password:', font=('arial 20 bold'),
                                 bg='light goldenrod yellow')
lbllength.grid(row=1, column=0)

entryenght = Entry(root, width=35, font=('arial 20 bold'), bg='white', textvariable=pass_leng)
entryenght.grid(row=1, column=1)
entryenght.focus_set()

lblgenerated= Label(root, width=30, text='Generated Password:', font=('arial 20 bold'),
                               bg='light goldenrod yellow')
lblgenerated.grid(row=2, column=0)

entrygenerated = Entry(root, width=35, font=('arial 20 bold'), bg='white')
entrygenerated.grid(row=2, column=1)

generatepassword = Button(text="Generate Password", width=30, bd=4, relief='solid',  font='arial 20 bold',
                  fg='black', bg='light goldenrod yellow', command=generate_pass)
generatepassword.grid(row=3, column=0)

reset = Button(text="Reset", width=30, bd=4, relief='solid', font='arial 20 bold', fg='black',
               bg='light goldenrod yellow', command=reset)
reset.grid(row=3, column=1)

root.mainloop()