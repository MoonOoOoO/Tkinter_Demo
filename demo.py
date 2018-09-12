import tkinter as tk

window = tk.Tk()
window.title('Tkinter Demo')
window.geometry('1024x768')

var = tk.StringVar()

l = tk.Label(window,
             textvariable=var,
             bg='#CCCCCC',
             font=('Arial', 12),
             width=15, height=2
             )
l.pack()

on_hit = False


def hit_me():
    print('hit')
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('You hit me')
    else:
        on_hit = False
        var.set('')


btn = tk.Button(
    window,
    text='Button',
    activebackground='gray',
    bg='white',
    width=15,
    height=2,
    command=hit_me
)
btn.pack()

e = tk.Entry(
    window,
    show='*'
)
e.pack()


def insert_point():
    v = e.get()
    t.insert('insert', v)


def insert_end():
    v = e.get()
    t.insert('end', v)


b1 = tk.Button(
    window,
    text='insert point',
    width=15,
    height=2,
    command=insert_point
)
b1.pack()

b2 = tk.Button(
    window,
    text='insert end',
    width=15,
    height=2,
    command=insert_end
)
b2.pack()

t = tk.Text(
    window,
    height=2
)
t.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))

lb = tk.Listbox(
    window,
    listvariable=var2
)

list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(3)
lb.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var.set(value)


button = tk.Button(
    window,
    text='Print Selection',
    width=15, height=2,
    command=print_selection
)
button.pack()

var3 = tk.StringVar()

label = tk.Label(
    window,
    bg='green',
    width=20, height=2,
    text='empty'
)
label.pack()


def print_selection_r():
    label.config(text='You have selected ' + var3.get())


r1 = tk.Radiobutton(
    window,
    text='Option A',
    variable=var3,
    value='A',
    command=print_selection_r
)
r1.pack()
r2 = tk.Radiobutton(
    window,
    text='Option B',
    variable=var3,
    value='B',
    command=print_selection_r
)
r2.pack()
r3 = tk.Radiobutton(
    window,
    text='Option C',
    variable=var3,
    value='C',
    command=print_selection_r
)
r3.pack()

window.mainloop()
