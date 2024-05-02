import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Sample Dash app
app = dash.Dash(__name__)

# Read the dataset
df = pd.read_excel(r'C:\Users\Yash\Desktop\BAP ISE\datasets\seAimlLab.xlsx')  # Adjust the file path accordingly

# Define layout
app.layout = html.Div(style={'backgroundColor': 'black', 'padding': '50px'}, children=[
    html.H1("Monthly Attendance Comparison", style={'color': 'white', 'textAlign': 'center'}),
    
    # Dropdown menu to select dataset
    dcc.Dropdown(
        id='dataset-dropdown',
        options=[
            {'label': 'seAimlLab', 'value': 'seAimlLab.xlsx'},
            {'label': 'seAimlTheory', 'value': 'seAimlTheory.xlsx'},
            {'label': 'SeDsLab', 'value': 'SeDsLab.xlsx'},
            {'label': 'SeDsTheory', 'value': 'SeDsTheory.xlsx'},
            {'label': 'TeAimlLab', 'value': 'TeAimlLab.xlsx'},
            {'label': 'TeAimlTheory', 'value': 'TeAimlTheory.xlsx'},
        ],
        value='seAimlLab.xlsx',  # Default to the first dataset
        clearable=False,
        style={'width': '50%', 'margin': 'auto', 'color': 'white'}
    ),
    
    # Placeholder for the graph
    dcc.Graph(id='monthly-attendance-graph', style={'margin': 'auto', 'width': '80%', 'height': '600px'})
])

# Callback to update graph
@app.callback(
    Output('monthly-attendance-graph', 'figure'),
    [Input('dataset-dropdown', 'value')]
)
def update_graph(selected_dataset):
    # Read the selected dataset
    df = pd.read_excel(f'C:/Users/Yash/Desktop/BAP ISE/datasets/{selected_dataset}')
    
    # Check if the required columns exist in the DataFrame
    if 'Month' in df.columns and 'Attendance' in df.columns:
        # Group data by month and calculate mean attendance
        monthly_attendance = df.groupby('Month')['Attendance'].mean().reset_index()
        
        # Create a bar chart with custom styling
        fig = go.Figure()
        fig.add_trace(go.Bar(x=monthly_attendance['Month'], y=monthly_attendance['Attendance'],
                             marker_color='rgb(55, 83, 109)'))
        fig.update_layout(
            title_text='Monthly Attendance Comparison',  # Set title text
            xaxis_title='Month',
            yaxis_title='Attendance',
            plot_bgcolor='navy',  # Set plot background color
            paper_bgcolor='navy',  # Set paper background color
            font=dict(color='white'),  # Set font color
        )
        return fig
    else:
        return go.Figure(data=[])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
