from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyApRDFW_LWlmChdsxpvDO7sRkR8Z7O6Bvc",
    "authDomain": "observatorio-4444b.firebaseapp.com",
    "databaseURL": "https://observatorio-4444b-default-rtdb.firebaseio.com",
    "storageBucket": "observatorio-4444b.appspot.com",
}

# here we are doing firebase authentication
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def index(request):
    return render(request, 'index.html')


def vih(request):
    casosxano2018 = database.child('VIH').child('CasosXano').child('2018').get().val()
    casosxano2019 = database.child('VIH').child('CasosXano').child('2019').get().val()
    casosxano2020 = database.child('VIH').child('CasosXano').child('2020').get().val()
    casosxano2021 = database.child('VIH').child('CasosXano').child('2021').get().val()
    casosxano2022 = database.child('VIH').child('CasosXano').child('2022').get().val()
    casosxano2023 = database.child('VIH').child('CasosXano').child('2023').get().val()
    casosxano2024 = database.child('VIH').child('CasosXano').child('2024').get().val()

    context = {
        'casosxano2018': casosxano2018,
        'casosxano2019': casosxano2019,
        'casosxano2020': casosxano2020,
        'casosxano2021': casosxano2021,
        'casosxano2022': casosxano2022,
        'casosxano2023': casosxano2023,
        'casosxano2024': casosxano2024,
    }

    return render(request, 'vih.html', context)
