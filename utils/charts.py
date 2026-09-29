import plotly.express as px
import plotly.graph_objects as go

def plot_energy_trend(df):
    """Line chart comparing Actual vs. Predicted energy usage over time."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Actual'], mode='lines', 
                             name='Actual Consumption (kWh)', line=dict(color='#00b4d8', width=2)))
    
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Predicted'], mode='lines', 
                             name='Predicted Consumption (kWh)', line=dict(color='#f72585', width=2, dash='dash')))
                             
    fig.update_layout(
        title="Energy Consumption Trend (Actual vs Predicted)",
        xaxis_title="Time",
        yaxis_title="Energy Consumption (kWh)",
        template="plotly_dark",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_appliance_usage(df):
    """Donut chart for usage by appliance."""
    fig = px.pie(df, values='Consumption (kWh)', names='Appliance', hole=0.5,
                 color_discrete_sequence=px.colors.qualitative.Pastel)
                 
    fig.update_layout(
        title="Usage by Appliance",
        template="plotly_dark",
        margin=dict(l=20, r=20, t=50, b=20)
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def plot_peak_hours(df):
    """Bar chart showing hourly consumption breakdown and highlighting peak hours."""
    # Add hour column for aggregation
    df['Hour'] = df['Timestamp'].dt.hour
    hourly_avg = df.groupby('Hour')['Actual'].mean().reset_index()
    
    # Define colors (highlight peak hours 12-16 i.e., 12 PM - 4 PM)
    colors = ['#f72585' if 12 <= h <= 16 else '#4cc9f0' for h in hourly_avg['Hour']]
    
    fig = go.Figure(data=[
        go.Bar(x=hourly_avg['Hour'], y=hourly_avg['Actual'], marker_color=colors)
    ])
    
    fig.update_layout(
        title="Average Hourly Consumption (Peak Hours Highlighted)",
        xaxis_title="Hour of Day (0-23)",
        yaxis_title="Avg Consumption (kWh)",
        template="plotly_dark",
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis=dict(tickmode='linear', tick0=0, dtick=1)
    )
    return fig
