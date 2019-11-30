from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('simNote')
root.iconbitmap('img/simNote.ico')
root.geometry('800x600+120+200')

textframe = Frame(root, bg='#3C3F41')
textframe.pack(fill=BOTH, expand=1)

# Navigation menu

top_nav = Menu(root)
root.config(menu=top_nav)

def del_str():
    textarea.delete('1.0', END)


def about():
    messagebox.showinfo('About simNote', 'Программа simNote, версия 1.0')


def theme_changer(theme):
    textarea['bg'] = themes[theme]['text_bg']
    textarea['fg'] = themes[theme]['text_fg']
    textarea['insertbackground'] = themes[theme]['cursor']
    textarea['selectbackground'] = themes[theme]['select_bg']


def root_quit():
    answer = messagebox.askokcancel(title='Выход', message='Закрыть программу?')
    if answer:
        root.destroy()


def file_open():
    file_path = filedialog.askopenfilename(title='Открыть файл', filetypes=(('Текстовые файлы(*.txt)', '*.txt'), ('Все файлы(*.*)', '*.*')))
    if file_path:
        textarea.delete('1.0', END)
        textarea.insert('1.0', open(file_path, encoding='utf-8').read())


def file_save():
    file_path = filedialog.asksaveasfilename(title='Сохранить файл', filetypes=(('Текстовые файлы(*.txt)', '*.txt'), ('Все файлы(*.*)', '*.*')))
    newfile = open(file_path, 'w', encoding='utf-8')
    text = textarea.get('1.0', END)
    newfile.write(text)
    newfile.close()


def file_save_as():
    file_path = filedialog.asksaveasfilename(title='Сохранить файл как', filetypes=(('Текстовые файлы(*.txt)', '*.txt'), ('Все файлы(*.*)', '*.*')))
    newfile = open(file_path, 'w', encoding='utf-8')
    text = textarea.get('1.0', END)
    newfile.write(text)
    newfile.close()


# File nav

file_nav = Menu(top_nav, tearoff=0)
file_nav.add_command(label='Создать')
file_nav.add_command(label='Открыть', command=file_open)
file_nav.add_command(label='Сохранить', command=file_save)
file_nav.add_command(label='Сохранить как', command=file_save_as)
file_nav.add_separator()
file_nav.add_command(label='Выход', command=root_quit)
top_nav.add_cascade(label='Файл', menu=file_nav)

# Edit nav

edit_nav = Menu(top_nav, tearoff=0)
edit_nav.add_command(label='Удалить спарава')
edit_nav.add_command(label='Удалить строку', command=del_str)
edit_nav.add_separator()
edit_nav.add_command(label='Отменить')
edit_nav.add_command(label='Метка')
edit_nav.add_separator()
edit_subnav = Menu(edit_nav, tearoff=0)
edit_subnav.add_command(label='Скопировать')
edit_subnav.add_command(label='Вырезать')
edit_subnav.add_command(label='Вставить')
edit_nav.add_cascade(label='Копипаст', menu=edit_subnav)
top_nav.add_cascade(label='Редактировать', menu=edit_nav)

# Themes

themes = {
    'dark': {
        'text_bg': '#343d46',
        'text_fg': '#cccccc',
        'cursor': '#ffffff',
        'select_bg': '#4e5a65',

    },
    'light': {
        'text_bg': '#ffffff',
        'text_fg': '#000000',
        'cursor': '#8000ff',
        'select_bg': '#777777',
    }
}

# Themes nav

themes_nav = Menu(top_nav, tearoff=0)
dev_subnav = Menu(themes_nav, tearoff=0)
themes_subnav = Menu(themes_nav, tearoff=0)
themes_subnav.add_command(label='Темное', command=lambda: theme_changer('dark'))
themes_subnav.add_command(label='Светлое', command=lambda: theme_changer('light'))
themes_nav.add_cascade(label='Оформление', menu=themes_subnav)
themes_nav.add_separator()
dev_subnav.add_command(label='Default')
dev_subnav.add_command(label='Цветное')
dev_subnav.add_command(label='Оригинальное')
dev_subnav.add_command(label='Темное(Visual Studio)')
dev_subnav.add_command(label='Светлое(Visual Studio)')
dev_subnav.add_command(label='Abyss')
dev_subnav.add_command(label='Solarized')
dev_subnav.add_command(label='Cobalt')
themes_nav.add_cascade(label='В разработке', menu=dev_subnav)
top_nav.add_cascade(label='Темы', menu=themes_nav)

# Help nav

help_nav = Menu(top_nav, tearoff=0)
theme_subnav = Menu(help_nav, tearoff=0)
theme_subnav.add_command(label='Онлайн')
theme_subnav.add_command(label='Оффлайн')
help_nav.add_cascade(label='Помощь', menu=theme_subnav)
help_nav.add_separator()
help_nav.add_command(label='О прграмме', command=about)
top_nav.add_cascade(label='Помощь', menu=help_nav)



textarea = Text(textframe, bg=themes['dark']['text_bg'], fg=themes['dark']['text_fg'], width=30, padx=10, pady=10, wrap=WORD, insertbackground=themes['dark']['cursor'], selectbackground=themes['dark']['select_bg'], spacing3=7)
# textarea = Text(textframe, bg='#343d46', fg='#cccccc', width=30, padx=10, pady=10, wrap=WORD, insertbackground='#eda756', selectbackground='#4e5a65', spacing3=5)
textarea.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(textframe, command=textarea.yview)
scroll.pack(fill=Y, side=LEFT)
textarea.config(yscrollcommand=scroll.set)

root.mainloop()