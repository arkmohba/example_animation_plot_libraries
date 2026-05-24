from steps import flux_upwind, step_with_flux
import numpy as np
import plotly.graph_objects as go

# データ
c = 1
dt = 0.005
dx = 0.01

jmax = int(21 * 0.1 / dx)
nmax = int(6 * 0.05 / dt)

x = np.linspace(0, dx * (jmax - 1), jmax)
q = np.zeros(jmax, dtype=float)
q[0:int(jmax/2)] = 1.0


fig = go.Figure(
    data=[
        go.Scatter(
            x=x,
            y=q,
            mode="lines"
        )
    ],
    layout=go.Layout(
        xaxis=dict(range=[0, dx * jmax]),
        yaxis=dict(range=[-1.5, 1.5]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50},
                                "fromcurrent": True
                            }
                        ]
                    }
                ]
            }
        ]
    ),
    frames=[
        go.Frame(
            data=[
                go.Scatter(
                    x=x,
                    y=step_with_flux(q, c, dt, dx, flux_upwind)
                )
            ]
        )
        for t in range(1000)
    ]
)

fig.show()
