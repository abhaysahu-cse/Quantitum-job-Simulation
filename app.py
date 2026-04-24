from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Placeholder layout — replace with actual data and charts
app.layout = html.Div(children=[
    html.H1("Quantium Data Visualisation"),
    html.P("Development environment is ready. Add your data and charts here."),
    dcc.Graph(
        id="example-graph",
        figure=px.bar(
            pd.DataFrame({"Category": ["A", "B", "C"], "Value": [10, 20, 15]}),
            x="Category",
            y="Value",
            title="Example Chart"
        )
    )
])

if __name__ == "__main__":
    app.run(debug=True)
