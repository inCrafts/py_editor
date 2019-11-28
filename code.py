from tkinter import *

root = Tk()
root.title('Editor')
root.geometry('800x600+120+200')

f_menu = Frame(root, bg='#1f252a', height=40)
f_text = Frame(root, bg='#3C3F41')
f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand=1)

l_menu = Label(f_menu, text='Menu', bg='#2b3239', fg='#cccccc', font='Arial 10').place(x=10, y=10)


def add_str():
    textarea.insert('2.4', 'Hello')


def del_str():
    textarea.delete('1.0', END)


def get_str():
    print(textarea.get('1.0', END))


btn_add  = Button(root, text='Add', command=add_str).place(x=50, y=10)
btn_del  = Button(root, text='Delete', command=del_str).place(x=90, y=10)
btn_get  = Button(root, text='Get', command=get_str).place(x=140, y=10)

textarea = Text(f_text, bg='#343d46', fg='#cccccc', width=30, padx=10, pady=10, wrap=WORD, insertbackground='#eda756', selectbackground='#4e5a65', spacing3=5)
textarea.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=textarea.yview)
scroll.pack(fill=Y, side=LEFT)
textarea.config(yscrollcommand=scroll.set)

root.mainloop()
