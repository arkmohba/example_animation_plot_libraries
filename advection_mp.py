from steps import flux_upwind, step_with_flux
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import scienceplots
# plt.style.use(["science"])

# データ
c = 1
dt = 0.005
dx = 0.01

jmax = int(21 * 0.1 / dx)
nmax = int(6 * 0.05 / dt)

x = np.linspace(0, dx * (jmax - 1), jmax)
q = np.zeros(jmax, dtype=float)
q[0:int(jmax/2)] = 1.0

fig, ax = plt.subplots()

line, = ax.plot(x, q)

ax.set_ylim(-1.5, 1.5)

def update(_):
    global q
    q = step_with_flux(q, c, dt, dx, flux_upwind)
    line.set_ydata(q)
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=None,
    cache_frame_data=False,
    interval=50,
    blit=True
)

plt.show()
input()

