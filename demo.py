import tkinter as tk

window = tk.Tk()
window.title('Tkinter Demo')
window.geometry('1366x1024')

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
var2.set((11, 22, 33))

lb = tk.Listbox(
    window,
    listvariable=var2
)

list_items = [1, 2, 3]
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
    bg='yellow',
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


def print_selection_s(v):
    label.config(text='You have selected ' + v)


s = tk.Scale(
    window,
    labe='Scale Slider',
    from_=5, to=15,
    orient=tk.HORIZONTAL,
    length=200, showvalue=0,
    tickinterval=2, resolution=0.01,
    command=print_selection_s
)
s.pack()

v1 = tk.IntVar()
v2 = tk.IntVar()


def print_selection_c():
    if (v1.get() == 1) & (v2.get() == 0):
        label.config(text='I love Python')
    elif (v1.get() == 0) & (v2.get() == 1):
        label.config(text='I love Java')
    elif (v1.get() == 0) & (v2.get() == 0):
        label.config(text='I don\'t love either')
    else:
        label.config(text='I love both')


c1 = tk.Checkbutton(
    window,
    text='Python',
    variable=v1,
    onvalue=1, offvalue=0,
    command=print_selection_c
)
c1.pack()
c2 = tk.Checkbutton(
    window,
    text='Java',
    variable=v2,
    onvalue=1, offvalue=0,
    command=print_selection_c
)
c2.pack()

canvas = tk.Canvas(
    window,
    bg='#cccccc',
    height=100, width=200
)
canvas.pack()

img_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=img_file)

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)


def move_it():
    canvas.move(rect, 4, 2)


btn1 = tk.Button(
    window,
    text='move rect',
    command=move_it
)
btn1.pack()
window.mainloop()
