from matplotlib import pyplot as plt
import numpy as np


# fig, ax = plt.subplots()
# ax.plot(np.random.rand(10))
#
#
# def onclick(event):
#     print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
#           ('double' if event.dblclick else 'single', event.button,
#            event.x, event.y, event.xdata, event.ydata))
#
#
# cid = fig.canvas.mpl_connect('button_press_event', onclick)
# plt.show()


class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        # print(event)
        if event.inaxes != self.line.axes:
            return
        self.xs.append(event.xdata)
        # print(self.xs)
        self.ys.append(event.ydata)
        # print(self.ys)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(411)
l, = ax.plot([0], [0])
line_builder = LineBuilder(l)


class DraggableRectangle:
    def __init__(self, rect):
        self.rect = rect
        self.press = None
        self.cidMotion = self.rect.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.cidRelease = self.rect.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidPress = self.rect.figure.canvas.mpl_connect('button_press_event', self.on_press)

    def on_press(self, event):
        """on button press we will see if the mouse is over us and store some data"""
        if event.inaxes != self.rect.axes:
            return
        contains, attr = self.rect.contains(event)
        # print(contains)
        if not contains:
            return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata

    def on_motion(self, event):
        """on motion we will move the rect if the mouse is over us"""
        if self.press is None:
            return
        if event.inaxes != self.rect.axes:
            return
        x0, y0, x_press, y_press = self.press
        dx = event.xdata - x_press
        dy = event.ydata - y_press
        # print('x0=%f, x_press=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #       (x0, x_press, event.xdata, dx, x0 + dx))
        self.rect.set_x(x0 + dx)
        self.rect.set_y(y0 + dy)

        self.rect.figure.canvas.draw()

    def on_release(self, event):
        """on release we reset the press data"""
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        """disconnect all the stored connection ids"""
        self.rect.figure.canvas.mpl_disconnect(self.cidPress)
        self.rect.figure.canvas.mpl_disconnect(self.cidRelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidMotion)


bx = fig.add_subplot(412)
rectangles = bx.bar(range(10), 20 * np.random.rand(10))
drs = []
for r in rectangles:
    dr = DraggableRectangle(r)
    drs.append(dr)


def enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()


def leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()


def enter_figure(event):
    print('enter_figure', event.inaxes)
    event.inaxes.patch.set_facecolor('red')
    event.canvas.draw()


def leave_figure(event):
    print('leave_figure', event.inaxes)
    event.inaxes.patch.set_facecolor('grey')
    event.canvas.draw()


# fig.canvas.mpl_connect('figure_enter_event', enter_figure)
# fig.canvas.mpl_connect('figure_leave_event', leave_figure)
# fig.canvas.mpl_connect('axes_enter_event', enter_axes)
# fig.canvas.mpl_connect('axes_leave_event', leave_axes)

cx = fig.add_subplot(413)
l_cx = cx.plot(np.random.randn(100), 'o', picker=5)


def onPick(event):
    this_line = event.artist
    xdata = this_line.get_xdata()
    ydata = this_line.get_ydata()
    ind = event.ind
    points = tuple(zip((xdata[ind], ydata[ind])))
    print(ind)
    print('onPick points: ', points)


cx.figure.canvas.mpl_connect('pick_event', onPick)

dx = fig.add_subplot(414)

plt.show()
