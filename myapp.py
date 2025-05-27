# %%
from dash import Dash, dcc, html, Input, Output  # Dash components you need
import plotly.express as px  # Dash relies on Plotly to actually do the plotting.  Plotly creates an HTML page with lots of JavaScript.
import plotly.data as pldata  # This is only needed to give access to the Plotly built in datasets.

df = pldata.stocks(indexed=False, datetimes=True)  # This loads one of the datasets

df_gap = pldata.gapminder(datetimes=True)
countries = df_gap["country"].unique()

# Initialize Dash app
app = Dash(
    __name__
)  # This creates the app object, to which various things are added below.
# __name__ is the name of the running Python module, which is your main module in this case

server = app.server  # <-- This is the line you need to add

# Layout: This section creates the HTML components
app.layout = html.Div(
    [  # This div is for the dropdown you see at the top, and also for the graph itself
        dcc.Dropdown(  # This creates the dropdown
            id="country-dropdown",
            options=[{"label": country, "value": country} for country in countries],
            value="Canada",  # Set a valid default country
        ),
        dcc.Graph(id="gdp-growth"),  # And the graph itself has to have an ID
    ]
)


# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")],
)
def update_graph(selected_country):
    filtered = df_gap[df_gap["country"] == selected_country]
    fig = px.line(
        filtered,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita Over Time - {selected_country}",
    )
    return fig


# Run the app
if (
    __name__ == "__main__"
):  # if this is the main module of the program, and not something included by a different module
    app.run(debug=True)  # start the Flask web server

# %%
