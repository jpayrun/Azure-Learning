
import json

from dash import Dash, callback, dcc, html, Input, Output
import plotly.express as ex

from pokemon import Pokemon, PokemonAPI

app = Dash(__name__)

app.layout = [
    html.H1(children="", id="pokemon-name"),
    dcc.Input(value = 7, type='number', min=1, max=151, id="pokemon-id"),
    html.Img(src="", id="pokemon-image"),
    # dcc.Store stores the intermediate value
    dcc.Store(id='intermediate-value')
]

@callback(
        Output('intermediate-value', 'data'),
        Input(component_property="value", component_id='pokemon-id')
)
def get_pokemon(id: int) -> str:
    pokemon = PokemonAPI().get_pokemon(id)
    data = {"name": pokemon.name,
            "stats" : pokemon.pokemon_stats(),
            "image": pokemon.images}
    return json.dumps(data)

@callback(
    Output("pokemon-name", "children"),
    Input('intermediate-value', 'data')
)
def pokemon_name(data: str):
    dataset = json.loads(data)
    name = dataset['name'][0].upper() + dataset['name'][1:]
    return name

@callback(
    Output("pokemon-image", "src"),
    Input('intermediate-value', 'data')
)
def pokemon_image(data):
    dataset = json.loads(data)
    return dataset['image']

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
    # app.run(debug=True)
