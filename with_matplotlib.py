import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# データ
x = np.linspace(0, 10, 200)
times = np.linspace(0, 4, 100)

fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1.5, 1.5)

def update(frame):
    y = np.sin(x - 0.04 * frame)
    line.set_ydata(y)
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
