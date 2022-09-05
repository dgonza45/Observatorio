import pandas as pd
from prophet import Prophet
import pyrebase
import requests
import os
import smtplib
import ssl
import json
import plotly.express as px

url = 'http://medata.gov.co/sites/default/files/medata_harvest_files/sivigila_vih.csv'
r = requests.get(url, allow_redirects=True)
open('vih.csv', 'wb').write(r.content)

file_stat = os.stat('vih.csv')

if file_stat.st_size < 300000:
    context = ssl.create_default_context()

    message = 'Se encontro un problema en la BD de VIH'
    subject = 'Error en base de datos de VIH'
    message = 'Subject: {}\n\n{}'.format(subject, message)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls(context=context)
    server.login('observatorioproyecto1@gmail.com', 'uwftzgqywensvpdm')
    server.sendmail('observatorioproyecto1@gmail.com', 'edango09@gmail.com', message)
    server.quit()
    exit()

config = {
    "apiKey": "AIzaSyApRDFW_LWlmChdsxpvDO7sRkR8Z7O6Bvc",
    "authDomain": "observatorio-4444b.firebaseapp.com",
    "databaseURL": "https://observatorio-4444b-default-rtdb.firebaseio.com",
    "storageBucket": "observatorio-4444b.appspot.com",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

data = pd.read_csv("vih.csv", sep=";")

# Variables para graficar
casos_por_ano = data.groupby(["year_"]).count()['id']
casos_por_ano_df = casos_por_ano.to_frame()
casos_por_ano_df.reset_index(inplace=True)
lista_casos_por_ano = casos_por_ano_df.values.tolist()
for i in range(10, 13):
    database.child('VIH').child("CasosXano").child(lista_casos_por_ano[i][0]).set(lista_casos_por_ano[i][1])

casos_edad = data.groupby(["edad_"]).count()['id']
casos_por_edad_df = casos_edad.to_frame()
casos_por_edad_df.reset_index(inplace=True)
lista_casos_edad = casos_por_edad_df.values.tolist()
for i in range(0, 80):
    database.child('VIH').child("CasosXedad").child(lista_casos_edad[i][0]).set(lista_casos_edad[i][1])

casos_sexo = data.groupby(["sexo_"]).count()['id']
casos_sexo_lista = casos_sexo.to_frame()
casos_sexo_lista.reset_index(inplace=True)
casos_sexo_lista = casos_sexo_lista.values.tolist()
for i in range(0, 2):
    database.child('VIH').child("CasosXsexo").child(casos_sexo_lista[i][0]).set(casos_sexo_lista[i][1])

casos_comuna = data.groupby(["comuna"]).count()['id']
casos_comuna_lista = casos_comuna.to_frame()
casos_comuna_lista.reset_index(inplace=True)
casos_comuna_lista = casos_comuna_lista.values.tolist()
for i in range(0, 28):
    database.child('VIH').child("CasosXcomuna").child(casos_comuna_lista[i][0]).set(casos_comuna_lista[i][1])

# Predicciones con prophet
# organizacion de las columnas a predecir
casos_por_ano_prediccion = casos_por_ano.to_frame()
casos_por_ano_prediccion.rename(columns={'id': "y"}, inplace=True)
casos_por_ano_prediccion.reset_index(inplace=True)
casos_por_ano_prediccion.rename(columns={'year_': "ds"}, inplace=True)
casos_por_ano_prediccion.ds.astype('int32')
casos_por_ano_prediccion['ds'] = pd.to_datetime(casos_por_ano_prediccion['ds'], format='%Y')
# modelo
m = Prophet()
m.fit(casos_por_ano_prediccion)
future = m.make_future_dataframe(periods=5, freq='Y')
forecast = m.predict(future)

# Convierte el tipo de las columnas
convert_dict = {'ds': str,
                'yhat': int}
forecast = forecast.astype(convert_dict)
prediccion = forecast[['ds', 'yhat']].tail(5).values.tolist()
for i in range(1, 5):
    database.child('VIH').child("CasosXano").child(prediccion[i][0][0:4]).set(prediccion[i][1])

# SISTEMA DE MAPAS

comunas_medellin = json.load(open("./planeacion_gdb.geojson"))

# Filtraccion de datos
casos_comuna = data.groupby(["comuna"]).count()['id']
casos_comuna = data.groupby(["comuna"]).count()['id']
casos_comuna_lista = casos_comuna.to_frame()
casos_comuna_lista.drop("Sin informacion", inplace=True)
casos_comuna_lista.drop("SIN INFORMACION", inplace=True)
casos_comuna_lista.reset_index(inplace=True)
casos_comuna_lista

# Correccion nombres comunas
casos_comuna_lista.at[23, 'comuna'] = 'San Sebastian de Palmitas'
comunas_medellin['features'][14]['properties']['NOMBRE'] = 'Belen'
comunas_medellin['features'][11]['properties']['NOMBRE'] = 'La America'
comunas_medellin['features'][10]['properties']['NOMBRE'] = 'Laureles'
comunas_medellin['features'][16]['properties']['NOMBRE'] = 'Corregimiento de San Cristobal'
comunas_medellin['features'][15]['properties']['NOMBRE'] = 'Corregimiento de Palmitas'

# Creacion mapa
mapa = px.choropleth_mapbox(casos_comuna_lista, geojson=comunas_medellin, locations="comuna",
                            featureidkey='properties.NOMBRE'
                            , color='id', mapbox_style="carto-positron", zoom=10.5,
                            center={"lat": 6.25184, "lon": -75.56359},
                            labels={'id': 'Casos de VIH'}, opacity=0.5)
mapa.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Exportat mapa
mapa.write_html('../../FRONT/obsfront/templates/mapa_vih.html')
