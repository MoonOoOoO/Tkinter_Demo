import numpy as np
import tkinter as tk
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
x = np.arange(-7, 7, 0.1)
y = x * x
ax.plot()
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)

# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))

# 把绘制的图形显示到tkinter窗口上
canvas = FigureCanvasTkAgg(fig, master=frmCanvas)
canvas.draw()
canvas.get_tk_widget().pack()


# 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
# toolbar = NavigationToolbar2Tk(canvas, window)
# toolbar.update()

# canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH)


def _quit():
    window.destroy()
    window.quit()


btn1 = tk.Button(
    frmBtn, text='Quit1', command=_quit,
    width=12, height=2
)
btn1.grid(column=0, row=0, pady=20, padx=20)

btn2 = tk.Button(
    frmBtn, text='Quit2', command=_quit,
    width=12, height=2
)
btn2.grid(column=1, row=0, pady=20, padx=20)

btn3 = tk.Button(
    frmBtn, text='Quit3', command=_quit,
    width=12, height=2
)
btn3.grid(column=2, row=0, pady=20, padx=20)

rd1 = tk.Checkbutton(
    frmBtn, text='Radio one', onvalue=1, offvalue=0,
)
rd1.grid(column=3, row=0)

tk.mainloop()
