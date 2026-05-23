import numpy as np
import plotly.graph_objects as go

# 空間
x = np.linspace(0, 10, 200)

# 時間
times = np.linspace(0, 4, 100)

# 初期データ
y0 = np.sin(x)

fig = go.Figure(
    data=[
        go.Scatter(
            x=x,
            y=y0,
            mode="lines"
        )
    ],
    layout=go.Layout(
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[-1.5, 1.5]),
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 50},
                                "fromcurrent": True
                            }
                        ]
                    )
                ]
            )
        ]
    ),
    frames=[
        go.Frame(
            data=[
                go.Scatter(
                    x=x,
                    y=np.sin(x - t)
                )
            ]
        )
        for t in times
    ]
)

fig.show()
