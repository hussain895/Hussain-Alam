from dash import Dash, html, dcc, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

# Generate sample data
np.random.seed(42)
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": np.random.randint(200, 700, size=6),
    "Profit": np.random.randint(50, 300, size=6)
})

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Advanced Interactive Dashboard", style={'textAlign': 'center'}),

    # Dropdown to select data
    html.Label("Select Data Type:", style={'fontWeight': 'bold'}),
    dcc.Dropdown(
        id="data-type",
        options=[
            {"label": "Sales", "value": "Sales"},
            {"label": "Profit", "value": "Profit"}
        ],
        value="Sales",
        clearable=False,
        style={"width": "40%"}
    ),

    # Slider for range selection
    html.Label("Select Month Range:", style={'fontWeight': 'bold', 'marginTop':'20px'}),
    dcc.Slider(
        min=1,
        max=len(df),
        step=1,
        value=len(df),
        marks={i: df.Month[i-1] for i in range(1, len(df)+1)},
        id='range-slider'
    ),

    # Plotly graph
    dcc.Graph(id="line-chart"),

    # Seaborn Heatmap
    html.H3("Correlation Heatmap (Seaborn)", style={'textAlign': 'center', 'marginTop':'30px'}),
    html.Img(id="heatmap", style={'display': 'block', 'margin': 'auto'})
])

# Callback to update chart and heatmap
@app.callback(
    Output("line-chart", "figure"),
    Output("heatmap", "src"),
    Input("data-type", "value"),
    Input("range-slider", "value")
)
def update_dashboard(data_type, range_val):
    # Filter data
    filtered_df = df.head(range_val)

    # Plotly line chart
    fig = px.line(filtered_df, x="Month", y=data_type, markers=True, title=f"{data_type} Trend")

    # Seaborn correlation heatmap
    corr = filtered_df.corr()
    plt.figure(figsize=(5,4))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("utf8")
    src = f"data:image/png;base64,{data}"

    return fig, src

if __name__ == "__main__":
    app.run(debug=True)
