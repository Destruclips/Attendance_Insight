import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

# Read the dataset
df_a = pd.read_excel(r'C:\Users\Yash\Desktop\BAP ISE\datasets\seAimlLab.xlsx')  # Adjust the file path accordingly
df_b = pd.read_excel(r'C:\Users\Yash\Desktop\BAP ISE\datasets\seAimlLab.xlsx')  # Adjust the file path accordingly
df_c = pd.read_excel(r'C:\Users\Yash\Desktop\BAP ISE\datasets\seAimlLab.xlsx')  # Adjust the file path accordingly

# Define layout for visualization A
layout_a = html.Div(style={'backgroundColor': 'black', 'padding': '50px'}, children=[
    html.H1("Attendance Distribution", style={'color': 'white', 'textAlign': 'center'}),
    
    # Dropdown menu to select dataset
    dcc.Dropdown(
        id='dataset-dropdown-a',
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
    dcc.Graph(id='attendance-distribution-graph-a', style={'margin': 'auto', 'width': '80%', 'height': '600px'})
])

# Define layout for visualization B
layout_b = html.Div(style={'backgroundColor': 'black', 'padding': '50px'}, children=[
    html.H1("Monthly Attendance Comparison", style={'color': 'white', 'textAlign': 'center'}),
    
    # Dropdown menu to select dataset
    dcc.Dropdown(
        id='dataset-dropdown-b',
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
    dcc.Graph(id='monthly-attendance-graph-b', style={'margin': 'auto', 'width': '80%', 'height': '600px'})
])

# Define layout for visualization C
layout_c = html.Div(style={'backgroundColor': 'black', 'padding': '50px'}, children=[
    html.H1("Overall Attendance Trends", style={'color': 'white', 'textAlign': 'center'}),
    
    # Dropdown menu to select dataset
    dcc.Dropdown(
        id='dataset-dropdown-c',
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
    dcc.Graph(id='overall-attendance-graph-c', style={'margin': 'auto', 'width': '80%', 'height': '600px'})
])

# Callback to update graph A
@app.callback(
    Output('attendance-distribution-graph-a', 'figure'),
    [Input('dataset-dropdown-a', 'value')]
)
def update_graph_a(selected_dataset):
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
        return go.Figure(data=[])

# Callback to update graph B
@app.callback(
    Output('monthly-attendance-graph-b', 'figure'),
    [Input('dataset-dropdown-b', 'value')]
)
def update_graph_b(selected_dataset):
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

# Callback to update graph C
@app.callback(
    Output('overall-attendance-graph-c', 'figure'),
    [Input('dataset-dropdown-c', 'value')]
)
def update_graph_c(selected_dataset):
    # Read the selected dataset
    df = pd.read_excel(f'C:/Users/Yash/Desktop/BAP ISE/datasets/{selected_dataset}')
    
    # Check if the required columns exist in the DataFrame
    if 'Month' in df.columns and 'Attendance' in df.columns:
        # Create a line chart for overall attendance trends with custom style
        fig = px.line(df, x='Month', y='Attendance', title='Overall Attendance Trends')
        fig.update_traces(line=dict(color='cyan', width=3))  # Update line color and width
        fig.update_layout(
            plot_bgcolor='navy',  # Set plot background color
            paper_bgcolor='navy',  # Set paper background color
            font=dict(color='white'),  # Set font color
            xaxis=dict(showgrid=False),  # Hide gridlines on x-axis
            yaxis=dict(showgrid=False),  # Hide gridlines on y-axis
            title=dict(font=dict(color='white')),  # Set title font color
        )
        return fig
    else:
        return px.scatter(title="No Data", labels={'x': 'Month', 'y': 'Attendance'})

# Define the layout of the app
app.layout = html.Div([
    
    # Use the Tailwind CSS CDN
    html.Link(
        rel='stylesheet',
        href='https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css'
    ),
    # Create a navbar
    html.Div(className="bg-gray-900 text-yellow-300 min-h-screen bg-cover ", children=[
        html.Nav(className="flex justify-between items-center border-b border-gray-800 p-4", children=[
            html.H1('BAP ISE PROJECT', className='ml-5 text-5xl font-bold'),
            html.Div(className="flex gap-5 mr-5", children=[
                html.Button('Attendance Distribution', id='button-a', n_clicks=0, className='p-2  border-2 rounded-md bg-gray-800 hover:text-gray-400 focus:outline-none '),
                html.Button('Monthly Attendance Comparison', id='button-b', n_clicks=0, className='p-2 -ml-2 border-2 rounded-md bg-gray-800 hover:text-gray-400 focus:outline-none'),
                html.Button('Overall Attendance Trends', id='button-c', n_clicks=0, className='p-2 -ml-2 border-2 rounded-md bg-gray-800 hover:text-gray-400 focus:outline-none')
            ])
        ]),
    
        html.Div(id='output-container', className='p-4')
    ])
    
])

# Define the callback to switch between the three buttons
@app.callback(
    Output('output-container', 'children'),
    [Input('button-a', 'n_clicks'),
     Input('button-b', 'n_clicks'),
     Input('button-c', 'n_clicks')]
)
def update_output(button_a_clicks, button_b_clicks, button_c_clicks):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'button-a' in changed_id:
        return layout_a
    elif 'button-b' in changed_id:
        return layout_b
    elif 'button-c' in changed_id:
        return layout_c
    else:
        return html.Div()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
