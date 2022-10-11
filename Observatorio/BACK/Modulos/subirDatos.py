import pyrebase
import pandas as pd


def subirdatos(enfermedad):
    config = {
        "apiKey": "AIzaSyApRDFW_LWlmChdsxpvDO7sRkR8Z7O6Bvc",
        "authDomain": "observatorio-4444b.firebaseapp.com",
        "databaseURL": "https://observatorio-4444b-default-rtdb.firebaseio.com",
        "storageBucket": "observatorio-4444b.appspot.com",
    }
    firebase = pyrebase.initialize_app(config)
    firebase.auth()
    database = firebase.database()

    data = pd.read_csv(enfermedad + '.csv', sep=";", low_memory=False)

    casos_por_ano = data.groupby(["year_"]).count()['id']
    casos_por_ano_df = casos_por_ano.to_frame()
    casos_por_ano_df.reset_index(inplace=True)
    lista_casos_por_ano = casos_por_ano_df.values.tolist()
    x = len(lista_casos_por_ano)
    for i in range(x - 6, x):
        database.child(enfermedad).child("CasosXano").child(lista_casos_por_ano[i][0]).set(lista_casos_por_ano[i][1])

    casos_edad = pd.cut(data["edad_"], bins=[0, 5, 11, 18, 26, 59, 100],
                        labels=['0-5', '6-11', '12-18', '19-26', '27-59', '60-100'])
    casos_edad = casos_edad.groupby(casos_edad).count()
    casos_edad = casos_edad.to_frame()
    casos_edad = casos_edad.rename(columns={"edad_": "edad"})
    casos_edad = casos_edad.reset_index()
    lista_casos_edad = casos_edad.values.tolist()
    x = len(lista_casos_edad)
    for i in range(0, x):
        database.child(enfermedad).child("CasosXedad").child(lista_casos_edad[i][0]).set(lista_casos_edad[i][1])

    casos_sexo = data.groupby(["sexo_"]).count()['id']
    casos_sexo_lista = casos_sexo.to_frame()
    casos_sexo_lista.reset_index(inplace=True)
    casos_sexo_lista = casos_sexo_lista.values.tolist()
    for i in range(0, 2):
        database.child(enfermedad).child("CasosXsexo").child(casos_sexo_lista[i][0]).set(casos_sexo_lista[i][1])

    casos_comuna = data.groupby(["comuna"]).count()['id']
    casos_comuna_lista = casos_comuna.to_frame()
    casos_comuna_lista.reset_index(inplace=True)
    casos_comuna_lista = casos_comuna_lista.values.tolist()
    x = len(casos_comuna_lista)
    for i in range(0, x):
        database.child(enfermedad).child("CasosXcomuna").child(casos_comuna_lista[i][0]).set(casos_comuna_lista[i][1])
    return
