import json
import plotly.express as px
import pandas as pd
import numpy as np

def generarmapa(enfermedad, filtro):
    comunas_medellin = json.load(open("planeacion_gdb.geojson"))

    data = pd.read_csv(enfermedad + '.csv', sep=";", low_memory=False)
    if(filtro == 0):
        casos_comuna = data.groupby(["comuna"]).count()['id']
        casos_comuna_lista = casos_comuna.to_frame()
        casos_comuna_lista.drop("Sin informacion", inplace=True)
        casos_comuna_lista.drop("SIN INFORMACION", inplace=True)
        casos_comuna_lista.reset_index(inplace=True)
        
        casos_comuna_lista.at[23, 'comuna'] = 'San Sebastian de Palmitas'
        comunas_medellin['features'][14]['properties']['NOMBRE'] = 'Belen'
        comunas_medellin['features'][11]['properties']['NOMBRE'] = 'La America'
        comunas_medellin['features'][10]['properties']['NOMBRE'] = 'Laureles'
        comunas_medellin['features'][16]['properties']['NOMBRE'] = 'Corregimiento de San Cristobal'
        comunas_medellin['features'][15]['properties']['NOMBRE'] = 'Corregimiento de Palmitas'

        mapa = px.choropleth_mapbox(casos_comuna_lista, geojson=comunas_medellin, locations="comuna",
                                    featureidkey='properties.NOMBRE', color='id', mapbox_style="carto-positron", zoom=10.5,
                                    center={"lat": 6.25184, "lon": -75.56359},
                                    labels={'id': 'Casos de ' + enfermedad}, opacity=0.5)
        mapa.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        mapa.write_html('../FRONT/obsfront/templates/mapa_' + enfermedad + '.html')

        
      
    elif(filtro == 1):
        casos_comuna = data.groupby(["comuna"]).count()['id']
        casos_comuna = data.groupby(["comuna","sexo_"]).count()['id']
        casos_comuna_lista = casos_comuna.to_frame()
        casos_comuna_lista.drop("Sin informacion",inplace=True)
        casos_comuna_lista.drop("SIN INFORMACION",inplace=True)
        casos_comuna_lista.reset_index(inplace=True)
        casos_comuna_lista["sexo_"] = np.where(casos_comuna_lista["sexo_"] == "F", "Mujer", "Hombre")

        casos_comuna_lista.at[23, 'comuna'] = 'San Sebastian de Palmitas'
        comunas_medellin['features'][14]['properties']['NOMBRE'] = 'Belen'
        comunas_medellin['features'][11]['properties']['NOMBRE'] = 'La America'
        comunas_medellin['features'][10]['properties']['NOMBRE'] = 'Laureles'
        comunas_medellin['features'][16]['properties']['NOMBRE'] = 'Corregimiento de San Cristobal'
        comunas_medellin['features'][15]['properties']['NOMBRE'] = 'Corregimiento de Palmitas'
        
        
        mapa = px.choropleth_mapbox(casos_comuna_lista, geojson=comunas_medellin ,locations="comuna"
                                    ,featureidkey='properties.NOMBRE' ,color='sexo_',hover_name='id',  
                                    mapbox_style="carto-positron",zoom=10.5,center = {"lat": 6.25184, "lon": -75.56359}, 
                                    labels={'id':'Casos de VIH', 'sexo_': 'Casos por sexo' }, 
                                    color_discrete_sequence=px.colors.qualitative.Dark2)
        mapa.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        mapa.write_html('../FRONT/obsfront/templates/mapa_sexo_' + enfermedad + '.html')

    
    elif(filtro == 2):
        #aplicar filtros
        casos_comuna = data.groupby("comuna")["edad_"].mean()
        casos_comuna_lista = casos_comuna.to_frame()
        casos_comuna_lista.drop("Sin informacion",inplace=True)
        casos_comuna_lista.drop("SIN INFORMACION",inplace=True)
        casos_comuna_lista.reset_index(inplace=True)
        # Arreglar nombres
        casos_comuna_lista.at[23, 'comuna'] = 'San Sebastian de Palmitas'
        comunas_medellin['features'][14]['properties']['NOMBRE'] = 'Belen'
        comunas_medellin['features'][11]['properties']['NOMBRE'] = 'La America'
        comunas_medellin['features'][10]['properties']['NOMBRE'] = 'Laureles'
        comunas_medellin['features'][16]['properties']['NOMBRE'] = 'Corregimiento de San Cristobal'
        comunas_medellin['features'][15]['properties']['NOMBRE'] = 'Corregimiento de Palmitas'
        #Generar mapa
        mapa = px.choropleth_mapbox(casos_comuna_lista, geojson=comunas_medellin ,locations="comuna"
                                    ,featureidkey='properties.NOMBRE' ,color='edad_', 
                                    mapbox_style="carto-positron",zoom=10.5,center = {"lat": 6.25184, "lon": -75.56359}, 
                                    labels={'id':'Casos de VIH', 'sexo_': 'Casos por sexo', 'edad_': 'Edad promedio por comuna' } 
                                    )
        mapa.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        mapa.write_html('../FRONT/obsfront/templates/mapa_edad_' + enfermedad + '.html')
        
    return
