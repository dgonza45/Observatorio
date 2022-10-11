import json
import plotly.express as px
import pandas as pd


def generarmapa(enfermedad):
    comunas_medellin = json.load(open("planeacion_gdb.geojson"))

    data = pd.read_csv(enfermedad + '.csv', sep=";", low_memory=False)

    casos_comuna = data.groupby(["comuna"]).count()['id']
    casos_comuna_lista = casos_comuna.to_frame()
    casos_comuna_lista.drop("Sin informacion", inplace=True)
    casos_comuna_lista.drop("SIN INFORMACION", inplace=True)
    casos_comuna_lista.reset_index(inplace=True)

    # Correccion nombres comunas
    casos_comuna_lista.at[23, 'comuna'] = 'San Sebastian de Palmitas'
    comunas_medellin['features'][14]['properties']['NOMBRE'] = 'Belen'
    comunas_medellin['features'][11]['properties']['NOMBRE'] = 'La America'
    comunas_medellin['features'][10]['properties']['NOMBRE'] = 'Laureles'
    comunas_medellin['features'][16]['properties']['NOMBRE'] = 'Corregimiento de San Cristobal'
    comunas_medellin['features'][15]['properties']['NOMBRE'] = 'Corregimiento de Palmitas'

    # Creacion mapa
    mapa = px.choropleth_mapbox(casos_comuna_lista, geojson=comunas_medellin, locations="comuna",
                                featureidkey='properties.NOMBRE', color='id', mapbox_style="carto-positron", zoom=10.5,
                                center={"lat": 6.25184, "lon": -75.56359},
                                labels={'id': 'Casos de ' + enfermedad}, opacity=0.5)
    mapa.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # Exportat mapa
    mapa.write_html('../FRONT/obsfront/templates/mapa_' + enfermedad + '.html')
    return
