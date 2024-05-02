import dash
from dash import html
from dash.dependencies import Input, Output
from a import app as layout_a
from b import app as layout_b
from c import app as layout_c

# Initialize the Dash app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

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
                html.Button('A', id='button-a', n_clicks=0, className='p-2  border-2 rounded-md bg-gray-800 hover:text-gray-400 focus:outline-none '),
                html.Button('B', id='button-b', n_clicks=0, className='p-2 -ml-2 border-2 rounded-md bg-gray-800 hover:text-gray-400 focus:outline-none'),
                html.Button('C', id='button-c', n_clicks=0, className='p-2 -ml-2 border-2 rounded-md bg-gray-800 hover:text-gray-400 focus:outline-none')
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
        return layout_a.layout
    elif 'button-b' in changed_id:
        return layout_b.layout
    elif 'button-c' in changed_id:
        return layout_c.layout
    else:
        return html.Div()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
