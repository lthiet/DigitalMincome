import plotly.graph_objects as go


def some_plot():
    # Create figure
    fig = go.Figure()

    # Range for each variable
    range_daily_volume = range(20)
    range_fee_percentage = range(100)
    range_yield_percentage = range(40)

    # Add traces, one for each slider step
    for step in range_daily_volume:
        fig.add_trace(
            go.Scatter(
                visible=False,
                x=[0],
                y=[0],
                mode="markers",
                marker_size=[step*10]))

    # Create a trace for each variable
    # add_traces(range_daily_volume)
    # add_traces(range_fee_percentage)
    # add_traces(range_yield_percentage)
    fig.data[-1].visible = True

    def create_steps(ranges):
        """
        Create steps
        """
        steps = []
        for i in range(len(ranges)):
            step = dict(
                method="update",
                args=[{"visible": [False] * len(ranges)},
                      {"title": "Slider switched to step: " + str(i)}],  # layout attribute
            )
            # Toggle i'th trace to "visible"
            step["args"][0]["visible"][i] = True
            steps.append(step)
        return steps

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Daily volume"},
        pad={"t": 50},
        steps=create_steps(range_daily_volume)
    )
    ]
    #  dict(
    #     active=10,
    #     currentvalue={"prefix": "Fee percentage"},
    #     pad={"t": 150},
    #     steps=create_steps(range(100))
    # ), dict(
    #     active=10,
    #     currentvalue={"prefix": "Yield percentage"},
    #     pad={"t": 250},
    #     steps=create_steps(range(50))
    # )]

    fig.update_layout(
        sliders=sliders
    )

    plot_html_path = 'data/plot.html'
    fig.write_html(plot_html_path)
    return "plot.html"