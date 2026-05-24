from steps import flux_upwind, step_with_flux
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

# データ
c = 1
dt = 0.005
dx = 0.01

jmax = int(21 * 0.1 / dx)
nmax = int(6 * 0.05 / dt)

x = np.linspace(0, dx * (jmax - 1), jmax)
q = np.zeros(jmax, dtype=float)
q[0:int(jmax/2)] = 1.0

app = pg.mkQApp()

win = pg.plot()
curve = win.plot()

def update():
    global q
    q = step_with_flux(q, c, dt, dx, flux_upwind)
    curve.setData(q)
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

win.show()

input()
