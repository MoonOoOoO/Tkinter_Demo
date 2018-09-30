import numpy as np
import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

points = []


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


matplotlib.use('TkAgg')
window = tk.Tk()
center_window(window, 800, 650)
frmBtn = tk.Frame(width=800, height=80, bg='gray')
frmCanvas = tk.Frame()
# frmCanvas = tk.Frame(width=800, height=450, bg='#CCCCCC')

frmBtn.grid(row=0, column=0, pady=20)
frmCanvas.grid(row=1, column=0)

frmBtn.grid_propagate(0)

fig = Figure(figsize=(8, 4))
ax = fig.add_subplot(111)
x = np.arange(-7, 7, 0.1)
y = x * x
ax.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# ax.set_xlim(-20, 20)
# ax.set_ylim(0, 50)

# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))

# 把绘制的图形显示到tkinter窗口上
canvas = FigureCanvasTkAgg(fig, master=frmCanvas)
canvas.draw()
canvas.get_tk_widget().pack()


def click_on_canvas(event):
    points.append([event.xdata, event.ydata])
    ax.plot([event.xdata], [event.ydata], 'ro')
    ax.figure.canvas.draw()
    print(points)


fig.canvas.mpl_connect('button_press_event', click_on_canvas)


def _quit():
    window.destroy()
    window.quit()
    quit()


global btn_i
btn_i = 0


def add_button(text, command):
    global btn_i
    btn = tk.Button(
        frmBtn, text=text, command=command,
        width=12, height=2
    )
    btn.grid(column=btn_i, row=0, pady=20, padx=20)
    btn_i = btn_i + 1


add_button('Quit1', _quit)
add_button('Quit2', _quit)
add_button('Quit3', _quit)
add_button('Quit4', _quit)

rd1 = tk.Checkbutton(
    frmBtn, text='Radio one', onvalue=1, offvalue=0,
)
rd1.grid(column=4, row=0)

tk.mainloop()
