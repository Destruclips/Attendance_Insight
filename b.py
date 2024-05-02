import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample Dash app
app = dash.Dash(__name__)

# Read the dataset
df = pd.read_excel(r'C:\Users\Yash\Desktop\BAP ISE\datasets\seAimlLab.xlsx')  # Adjust the file path accordingly

# Define layout
app.layout = html.Div(style={'backgroundColor': 'black', 'padding': '50px'}, children=[
    html.H1("Attendance Distribution", style={'color': 'white', 'textAlign': 'center'}),
    
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
    dcc.Graph(id='attendance-distribution-graph', style={'margin': 'auto', 'width': '80%', 'height': '600px'})
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('attendance-distribution-graph', 'figure'),
    [Input('dataset-dropdown', 'value')]
)
def update_graph(selected_dataset):
    # Read the selected dataset
    df = pd.read_excel(f'C:/Users/Yash/Desktop/BAP ISE/datasets/{selected_dataset}')
    
    # Check if the required column exists in the DataFrame
    if 'Attendance' in df.columns:
        # Create a histogram for attendance distribution with custom style
        fig = px.histogram(df, x='Attendance', title='Attendance Distribution')
        fig.update_layout(
            plot_bgcolor='navy',  # Set plot background color
            paper_bgcolor='navy',  # Set paper background color
            font=dict(color='white'),  # Set font color
            title=dict(font=dict(color='white')),  # Set title font color
        )
        return fig
    else:
        return px.scatter(title="No Data", labels={'x': 'Attendance'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
