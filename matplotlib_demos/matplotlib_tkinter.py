import matplotlib
import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

matplotlib.use('TkAgg')
window = tk.Tk()
window.wm_title("Embedding in TK")

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

figure = Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(311)
ax.plot(t, s)

ax.set(xlabel='time(s)', ylabel='voltage(mV)',
       title='About as simple as it gets, folks')

ax.grid()

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

bx = figure.add_subplot(312)
bx.plot(x1, y1, 'o-')
bx.set(ylabel='Damped oscillation')

cx = figure.add_subplot(313)
cx.plot(x2, y2, '.-')
bx.set(xlabel='time(s)', ylabel='Un-damped')

canvas = FigureCanvasTkAgg(figure, master=window)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, window)
toolbar.update()
canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def _quit():
    window.quit()
    window.destroy()
    quit()


button = tk.Button(
    window, text="Quit", command=_quit
)
button.pack(side=tk.BOTTOM)
window.mainloop()
