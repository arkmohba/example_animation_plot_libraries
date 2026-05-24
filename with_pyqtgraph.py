import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

app = pg.mkQApp()

win = pg.plot()
curve = win.plot()

x = np.linspace(0, 10, 1000)

i = 0

def update():
    global i
    curve.setData(np.sin(x - i * 0.1))
    i += 1

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

win.show()

input()
