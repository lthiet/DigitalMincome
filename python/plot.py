import plotly.express as px
import os

cwd = os.getcwd()
plot_html_path = os.path.join(os.path.dirname(cwd),'DigitalMincome/app/plot.html')



df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

fig["layout"].pop("updatemenus") # optional, drop animation buttons
fig.write_html(plot_html_path)
