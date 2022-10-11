import pandas as pd
from prophet import Prophet
import pyrebase


def predecir(enfermedad):
    config = {
        "apiKey": "AIzaSyApRDFW_LWlmChdsxpvDO7sRkR8Z7O6Bvc",
        "authDomain": "observatorio-4444b.firebaseapp.com",
        "databaseURL": "https://observatorio-4444b-default-rtdb.firebaseio.com",
        "storageBucket": "observatorio-4444b.appspot.com",
    }
    firebase = pyrebase.initialize_app(config)
    firebase.auth()
    database = firebase.database()

    data = pd.read_csv(enfermedad+'.csv', sep=";", low_memory=False)

    casos_por_ano = data.groupby(["year_"]).count()['id']
    casos_por_ano_df = casos_por_ano.to_frame()
    casos_por_ano_df.reset_index(inplace=True)
    casos_por_ano_prediccion = casos_por_ano.to_frame()
    casos_por_ano_prediccion.rename(columns={'id': "y"}, inplace=True)
    casos_por_ano_prediccion.reset_index(inplace=True)
    casos_por_ano_prediccion.rename(columns={'year_': "ds"}, inplace=True)
    casos_por_ano_prediccion.ds.astype('int32')
    casos_por_ano_prediccion['ds'] = pd.to_datetime(casos_por_ano_prediccion['ds'], format='%Y')

    m = Prophet()
    m.fit(casos_por_ano_prediccion)
    future = m.make_future_dataframe(periods=5, freq='Y')
    forecast = m.predict(future)
    convert_dict = {'ds': str,
                    'yhat': int}
    forecast = forecast.astype(convert_dict)
    prediccion = forecast[['ds', 'yhat']].tail(5).values.tolist()
    for i in range(1, 5):
        database.child(enfermedad).child("CasosXano").child(prediccion[i][0][0:4]).set(prediccion[i][1])
    return
