import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
#import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

data = pd.read_csv(r'C:\Users\Michael\Desktop\heart.csv')
data['count'] = list(range(data['age'].count()))


app = dash.Dash(__name__)

#-------------------------------------------------------------------------------------
app.layout = html.Div([

        html.Div([
            html.Pre(children= "Heart Disease",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ]),

        html.Div([
            html.Label(['X-axis categories to compare:'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': 'Target', 'value': 'target'},
                         {'label': 'Age', 'value': 'age'},
                         {'label': 'Sex', 'value': 'sex'},
                         {'label': 'The slope of the peak exercise ST segment', 'value': 'slope'},
                         {'label': 'Fasting blood sugar > 120 mg/dl', 'value': 'fbs'},
                         {'label': 'Chest pain type', 'value': 'cp'},
                         {'label': 'COunt', 'value': 'count'}
                ],
                value='Select smth',
                style={"width": "50%"}
            ),
        ]),

        html.Div([
            html.Br(),
            html.Label(['Y-axis values to compare:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='yaxis_raditem',
                options=[
                         {'label': 'Target', 'value': 'target'},
                         {'label': 'Age', 'value': 'age'},
                         {'label': 'Sex', 'value': 'sex'},
                         {'label': 'The slope of the peak exercise ST segment', 'value': 'slope'},
                         {'label': 'Fasting blood sugar > 120 mg/dl', 'value': 'fbs'},
                         {'label': 'Chest pain type', 'value': 'cp'},
                         {'label': 'COunt', 'value': 'count'}
                ],
                value='choose smth',
                style={"width": "50%"}
            ),
        ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),



])

#-------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)

def update_graph(x_axis, y_axis):

    dff = data

    # print(dff[[x_axis,y_axis]][:1])

    barchart=px.bar(
            data_frame=dff,
            x=x_axis,
            y=y_axis,
            title=y_axis+': by '+x_axis,
            #facet_col='target',
            color='target',
            barmode='stack',
            height=400
            )

    barchart.update_layout(xaxis={'categoryorder':'total ascending'},
                           title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,})

    return (barchart)

if __name__ == '__main__':
    app.run_server(debug=True)