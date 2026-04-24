import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc, callback, Output, Input

# --- Load and prepare data ---
df = pd.read_csv("output/processed_sales.csv", parse_dates=["date"])
df = df.sort_values("date")

PRICE_INCREASE_DATE = "2021-01-15"
REGIONS = ["all"] + sorted(df["region"].unique().tolist())

# --- App ---
app = Dash(__name__)

app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "maxWidth": "1100px", "margin": "0 auto", "padding": "20px"},
    children=[
        # Header
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#2c3e50", "marginBottom": "4px"},
        ),
        html.P(
            "Soul Foods — Impact of the Pink Morsel price increase on 15 January 2021",
            style={"textAlign": "center", "color": "#7f8c8d", "marginTop": "0", "marginBottom": "24px"},
        ),

        # Region filter
        html.Div(
            style={"display": "flex", "alignItems": "center", "gap": "12px", "marginBottom": "16px"},
            children=[
                html.Label("Filter by region:", style={"fontWeight": "bold", "color": "#2c3e50"}),
                dcc.RadioItems(
                    id="region-filter",
                    options=[{"label": r.capitalize(), "value": r} for r in REGIONS],
                    value="all",
                    inline=True,
                    inputStyle={"marginRight": "4px"},
                    labelStyle={"marginRight": "16px", "color": "#2c3e50"},
                ),
            ],
        ),

        # Line chart
        dcc.Graph(id="sales-chart", style={"height": "520px"}),

        # Footer note
        html.P(
            "The dashed red line marks the price increase date (15 Jan 2021).",
            style={"textAlign": "center", "color": "#95a5a6", "fontSize": "13px", "marginTop": "8px"},
        ),
    ],
)


@callback(Output("sales-chart", "figure"), Input("region-filter", "value"))
def update_chart(selected_region):
    if selected_region == "all":
        # Aggregate all regions by date
        plot_df = df.groupby("date", as_index=False)["sales"].sum()
        title_suffix = "All Regions"
    else:
        plot_df = df[df["region"] == selected_region].groupby("date", as_index=False)["sales"].sum()
        title_suffix = selected_region.capitalize()

    fig = go.Figure()

    # Sales line
    fig.add_trace(
        go.Scatter(
            x=plot_df["date"],
            y=plot_df["sales"],
            mode="lines",
            name="Daily Sales",
            line=dict(color="#2980b9", width=2),
            hovertemplate="<b>%{x|%d %b %Y}</b><br>Sales: $%{y:,.2f}<extra></extra>",
        )
    )

    # Vertical line for price increase
    fig.add_vline(
        x=PRICE_INCREASE_DATE,
        line_width=2,
        line_dash="dash",
        line_color="red",
        annotation_text="Price increase",
        annotation_position="top right",
        annotation_font_color="red",
    )

    fig.update_layout(
        title=dict(
            text=f"Pink Morsel Daily Sales — {title_suffix}",
            font=dict(size=18, color="#2c3e50"),
            x=0.5,
        ),
        xaxis=dict(
            title="Date",
            showgrid=True,
            gridcolor="#ecf0f1",
            tickformat="%b %Y",
        ),
        yaxis=dict(
            title="Sales (USD)",
            showgrid=True,
            gridcolor="#ecf0f1",
            tickprefix="$",
            tickformat=",.0f",
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=60, r=40, t=60, b=60),
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
