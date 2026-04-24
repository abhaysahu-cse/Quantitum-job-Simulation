import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc, callback, Output, Input

# ── Data ──────────────────────────────────────────────────────────────────────
df = pd.read_csv("output/processed_sales.csv", parse_dates=["date"])
df = df.sort_values("date")

PRICE_INCREASE_DATE = "2021-01-15"
REGIONS = ["all"] + sorted(df["region"].unique().tolist())

# Pre-compute headline stats (all regions combined)
total_before = df[df["date"] < PRICE_INCREASE_DATE]["sales"].sum()
total_after  = df[df["date"] >= PRICE_INCREASE_DATE]["sales"].sum()
pct_change   = ((total_after - total_before) / total_before) * 100

# ── App ───────────────────────────────────────────────────────────────────────
app = Dash(__name__)

app.layout = html.Div(
    className="page-wrapper",
    children=[

        # ── Hero header ──────────────────────────────────────────────────────
        html.Div(
            className="hero",
            children=[
                html.H1("🍬 Pink Morsel Sales Visualiser", className="hero-title"),
                html.P(
                    "Soul Foods · Analysing the impact of the Pink Morsel price increase · 15 January 2021",
                    className="hero-subtitle",
                ),
            ],
        ),

        # ── Stats bar ────────────────────────────────────────────────────────
        html.Div(
            className="stats-bar",
            children=[
                html.Div(className="stat-card", children=[
                    html.P("Sales before price increase", className="stat-label"),
                    html.P(f"${total_before:,.0f}", className="stat-value"),
                ]),
                html.Div(className="stat-card", children=[
                    html.P("Sales after price increase", className="stat-label"),
                    html.P(f"${total_after:,.0f}", className="stat-value"),
                ]),
                html.Div(className="stat-card", children=[
                    html.P("Change in sales", className="stat-label"),
                    html.P(
                        f"{pct_change:+.1f}%",
                        className="stat-value negative" if pct_change < 0 else "stat-value positive",
                    ),
                ]),
            ],
        ),

        # ── Chart card ───────────────────────────────────────────────────────
        html.Div(
            className="chart-card",
            children=[

                # Region filter
                html.Div(
                    className="filter-row",
                    children=[
                        html.Span("Region", className="filter-label"),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[{"label": r.capitalize(), "value": r} for r in REGIONS],
                            value="all",
                            className="region-radio",
                            inputStyle={"display": "none"},
                            labelStyle={},
                        ),
                    ],
                ),

                # Line chart
                dcc.Graph(
                    id="sales-chart",
                    config={"displayModeBar": False},
                    style={"height": "480px"},
                ),
            ],
        ),

        # ── Footer ───────────────────────────────────────────────────────────
        html.P(
            "The dashed line marks the Pink Morsel price increase on 15 Jan 2021. "
            "Data sourced from Soul Foods transaction records.",
            className="footer-note",
        ),
    ],
)


# ── Callback ──────────────────────────────────────────────────────────────────
@callback(Output("sales-chart", "figure"), Input("region-filter", "value"))
def update_chart(selected_region):
    if selected_region == "all":
        plot_df = df.groupby("date", as_index=False)["sales"].sum()
        region_label = "All Regions"
    else:
        plot_df = (
            df[df["region"] == selected_region]
            .groupby("date", as_index=False)["sales"]
            .sum()
        )
        region_label = selected_region.capitalize()

    fig = go.Figure()

    # Shaded area under the line
    fig.add_trace(
        go.Scatter(
            x=plot_df["date"],
            y=plot_df["sales"],
            mode="lines",
            fill="tozeroy",
            fillcolor="rgba(233, 30, 140, 0.08)",
            name="Daily Sales",
            line=dict(color="#e91e8c", width=2.5),
            hovertemplate="<b>%{x|%d %b %Y}</b><br>Sales: $%{y:,.0f}<extra></extra>",
        )
    )

    # Price increase vertical line (using shapes for broad Plotly compatibility)
    fig.add_shape(
        type="line",
        x0=PRICE_INCREASE_DATE, x1=PRICE_INCREASE_DATE,
        y0=0, y1=1,
        xref="x", yref="paper",
        line=dict(color="#e74c3c", width=2, dash="dash"),
    )
    fig.add_annotation(
        x=PRICE_INCREASE_DATE,
        y=0.97,
        xref="x", yref="paper",
        text="  Price increase ▲",
        showarrow=False,
        font=dict(color="#e74c3c", size=12, family="Inter"),
        xanchor="left",
    )

    fig.update_layout(
        title=dict(
            text=f"Daily Pink Morsel Sales — {region_label}",
            font=dict(size=17, color="#1a1a2e", family="Inter"),
            x=0.0,
            xanchor="left",
            pad=dict(l=4),
        ),
        xaxis=dict(
            title=dict(text="Date", font=dict(size=13, color="#888")),
            showgrid=True,
            gridcolor="#f0f0f0",
            tickformat="%b %Y",
            tickfont=dict(size=11, color="#888"),
            linecolor="#e0e0e0",
            zeroline=False,
        ),
        yaxis=dict(
            title=dict(text="Sales (USD)", font=dict(size=13, color="#888")),
            showgrid=True,
            gridcolor="#f0f0f0",
            tickprefix="$",
            tickformat=",.0f",
            tickfont=dict(size=11, color="#888"),
            linecolor="#e0e0e0",
            zeroline=False,
        ),
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#1a1a2e",
            font_color="#ffffff",
            font_size=13,
            bordercolor="#1a1a2e",
        ),
        showlegend=False,
        margin=dict(l=16, r=16, t=48, b=16),
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
